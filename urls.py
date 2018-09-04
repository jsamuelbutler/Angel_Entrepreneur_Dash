from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r'accelerators', views.AcceleratorViewSet)
router.register(r'cohorts', views.CohortViewSet)
