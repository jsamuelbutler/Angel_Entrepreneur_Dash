from __future__ import absolute_import

from outset import celery_app
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@celery_app.task
def accelerator_soft_delete_cascade(pk):
    logger.info('Starting accelerator_soft_delete_cascade({})...'.format(pk))

    from safedelete.config import SOFT_DELETE_CASCADE
    from outset.accelerators.models import Accelerator

    accelerator = Accelerator.objects.all_with_deleted().filter(pk=pk).first()
    if accelerator:
        logger.info('Cascade soft delete: {}'.format(accelerator))
        accelerator.delete(force_policy=SOFT_DELETE_CASCADE)


@celery_app.task
def cohort_soft_delete_cascade(pk):
    logger.info('Starting cohort_soft_delete_cascade({})...'.format(pk))

    from safedelete.config import SOFT_DELETE_CASCADE
    from outset.accelerators.models import Cohort

    cohort = Cohort.objects.all_with_deleted().filter(pk=pk).first()
    if cohort:
        logger.info('Cascade soft delete: {}'.format(cohort))
        cohort.delete(force_policy=SOFT_DELETE_CASCADE)
