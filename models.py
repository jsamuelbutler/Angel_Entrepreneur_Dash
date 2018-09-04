from __future__ import unicode_literals

from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from safedelete.config import SOFT_DELETE
from safedelete.models import SafeDeleteModel
from safedelete.signals import pre_softdelete

from outset.models import ModelDiffMixin

from .managers import AcceleratorManager, CohortManager
from .tasks import accelerator_soft_delete_cascade, cohort_soft_delete_cascade


class BaseOrganization(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    name = models.CharField(_('Name'), max_length=50, blank=True)
    logo = models.ImageField(_('Logo'), blank=True, null=True)
    website = models.URLField(_('Website'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Accelerator(ModelDiffMixin, BaseOrganization):
    objects = AcceleratorManager()

    def __str__(self):
        return '"{}" accelerator'.format(self.name)


class Cohort(ModelDiffMixin, SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    name = models.CharField(max_length=128)
    accelerator = models.ForeignKey(Accelerator, related_name='cohorts', on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    objects = CohortManager()

    def __str__(self):
        return '"{}" fund'.format(self.name)


@receiver(pre_softdelete, sender=Accelerator)
def cascade_soft_delete_accelerator(sender, instance, using, **kwargs):
    diff = instance.get_field_diff('deleted')
    if diff and diff[0] is None:
        accelerator_soft_delete_cascade.delay(instance.pk)


@receiver(pre_softdelete, sender=Cohort)
def cascade_soft_delete_cohort(sender, instance, using, **kwargs):
    diff = instance.get_field_diff('deleted')
    if diff and diff[0] is None:
        cohort_soft_delete_cascade.delay(instance.pk)
