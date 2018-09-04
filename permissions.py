from outset.accounts.models import User
from outset.permissions import IsModelSelfOrReadOnly

from .models import Accelerator, Cohort


class IsAcceleratorSelfOrReadOnly(IsModelSelfOrReadOnly):
    model = Accelerator
    user_field = 'accelerator_id'
    can_update_roles = (User.FOUNDER_ROLE, User.ADMIN_ROLE)


class IsCohortSelfOrReadOnly(IsModelSelfOrReadOnly):
    model = Cohort
    object_field = 'accelerator_id'
    user_field = 'accelerator_id'
    can_update_roles = (User.FOUNDER_ROLE, User.ADMIN_ROLE)
    can_create_roles = can_update_roles
