from django.db.models.query import Q
from safedelete.managers import SafeDeleteQueryset, SafeDeleteManager


class CohortQuerySet(SafeDeleteQueryset):
    def available_to_user(self, user):
        if user.is_anonymous():
            return self.none()
        account_type = user.account_type
        if account_type in (1, 2, 3):
            q = Q(accelerator_id=user.accelerator_id)
        elif account_type in (4, 5):
            return self.none()
        else:
            q = Q(id__in=user.cohorts_views.values('cohort_id'))
        return self.filter(q)


class AcceleratorQuerySet(SafeDeleteQueryset):
    def available_to_user(self, user):
        if user.is_anonymous():
            return self.none()
        account_type = user.account_type
        if account_type in (1, 2, 3):
            return self.filter(id=user.accelerator_id)
        return self.none()


class CohortManager(SafeDeleteManager):
    _queryset_class = CohortQuerySet

    def available_to_user(self, user):
        return self.get_queryset().available_to_user(user)


class AcceleratorManager(SafeDeleteManager):
    _queryset_class = AcceleratorQuerySet

    def available_to_user(self, user):
        return self.get_queryset().available_to_user(user)
