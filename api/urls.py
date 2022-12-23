from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()

router.register('super-makers', views.SuperMakerViewSet),
router.register('users', views.UserViewSet, basename='user')

router.register('groups', views.GroupViewSet)

router.register('model-prints', views.ModelPrintViewSet)
router.register('manufacturers', views.ManufacturerViewSet)
router.register('filament-rolls', views.FilamentRollViewSet)
router.register('filament-instances', views.FilamentInstanceViewSet)
router.register('filament-materials', views.FilamentMaterialViewSet)

urlpatterns = [

] + router.urls