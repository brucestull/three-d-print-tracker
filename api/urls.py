from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('groups', views.GroupViewSet, basename='groups')

router.register('basic-model-prints', views.BasicModelPrintViewSet)
router.register('basic-manufacturers', views.BasicManufacturerViewSet)
# router.register('hyper-manufacturers', views.HyperManufacturerViewSet)

urlpatterns = router.urls + [

]