from django.contrib import admin

from outset.startups.models import Startup

from .models import Accelerator, Cohort


class StartupInline(admin.TabularInline):
    model = Startup
    fields = ('name', 'amount_invested', 'security_type', 'ownership')
    extra = 1


@admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    inlines = (StartupInline,)
    search_fields = ('name',)


@admin.register(Accelerator)
class AcceleratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
