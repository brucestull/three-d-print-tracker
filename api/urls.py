from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

router.register('model-prints', views.ModelPrintViewSet)
router.register('manufacturers', views.ManufacturerViewSet)
router.register('filament-rolls', views.FilamentRollViewSet)

urlpatterns = router.urls + [

]