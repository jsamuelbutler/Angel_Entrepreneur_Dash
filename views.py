from __future__ import unicode_literals

from collections import OrderedDict, Counter
from decimal import Decimal

from django.db.models import F, Prefetch, Sum
from django.http.request import QueryDict
from django.urls import reverse
from rest_framework import filters, serializers, status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.settings import api_settings

from outset.activities.models import Activity
from outset.activities.serializers import ActivitySerializer
from outset.activities.views import ActivitiesPaginator
from outset.invitations.serializers import InviteAcceleratorTeamMemberSerializer
from outset.kpis.consts import VALUATION_KPI
from outset.kpis.models import KPI
from outset.startups.models import Startup
from outset.startups.serializers import TinyStartupSerializer

from .models import Accelerator, Cohort
from .permissions import IsAcceleratorSelfOrReadOnly, IsCohortSelfOrReadOnly
from .serializers import AcceleratorSerializer, CohortSerializer


class AcceleratorViewSet(viewsets.ModelViewSet):
    queryset = Accelerator.objects.prefetch_related('cohorts').all()
    serializer_class = AcceleratorSerializer
    pagination_class = None
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsAcceleratorSelfOrReadOnly]

    def get_queryset(self):
        return self.queryset.available_to_user(self.request.user)

    @detail_route(methods=['post'], serializer_class=InviteAcceleratorTeamMemberSerializer)
    def invite(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(accelerator=instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CohortViewSet(viewsets.ModelViewSet):
    queryset = Cohort.objects.all().order_by('name')
    serializer_class = CohortSerializer
    permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES + [IsCohortSelfOrReadOnly]
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name',)

    def get_queryset(self):
        return self.queryset.available_to_user(self.request.user)

    @detail_route(methods=['post'], serializer_class=serializers.Serializer)
    def invite(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(cohort=instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @detail_route(methods=['get'], serializer_class=serializers.Serializer)
    def portfolio_statistic(self, request, pk):
        instance = self.get_object()

        data = Counter()
        default = Decimal(0)
        startup_data = list(instance.startups.values_list('amount_invested', 'ownership'))
        for amount_invested, ownership in startup_data:
            data['amount_invested__sum'] += amount_invested or default
            data['ownership__avg'] += ownership or default
            data['initial_valuation__sum'] += (
                (100 * amount_invested / ownership)
                if ownership and amount_invested else
                default
            )
        if len(startup_data):
            data['ownership__avg'] /= len(startup_data)
        else:
            data['ownership__avg'] = Decimal(0)

        current_valuation = KPI.objects.filter(
            base__id=VALUATION_KPI, startup__in=instance.startups.all()
        ).with_value().aggregate(Sum('value'))['value__sum']
        current_valuation = current_valuation or default
        amt_invested = data['amount_invested__sum']
        avg_ownership = data['ownership__avg']
        statistic = [
            ('Amount Invested',   round(amt_invested)),
            ('Average Ownership', round(avg_ownership, 2)),
            ('Initial Valuation', round(data['initial_valuation__sum'])),
            ('Current Valuation', round(current_valuation)),
            ('Gain/Loss',         round(current_valuation*avg_ownership/100-amt_invested)),
        ]
        return Response(data=[{'text': k, 'count': v} for k, v in statistic])

    @detail_route(methods=['get'], serializer_class=serializers.Serializer)
    def activities(self, request, pk):
        data = []
        for i in Startup.objects.available_to_user(request.user).prefetch_related(
                    Prefetch('activity_set', queryset=Activity.objects.select_related('template').all())
                ).filter(cohort=pk):
            paginator = ActivitiesPaginator()
            activity_startup_filter = 'startup={}'.format(i.id)

            # Some request fix to generate correct links for startup activities
            request._request.path = reverse('activities-list')
            request._request.GET = QueryDict(activity_startup_filter)
            request._request.META['QUERY_STRING'] = activity_startup_filter

            results = paginator.paginate_queryset(i.activity_set.all(), request)
            data.append(OrderedDict([
                ('startup',  TinyStartupSerializer(i).data),
                ('count',    paginator.page.paginator.count),
                ('next',     paginator.get_next_link()),
                ('previous', paginator.get_previous_link()),
                ('results',  [ActivitySerializer(activity).data for activity in results]),
            ]))
        return Response(data=data)

