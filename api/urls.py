from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('groups', views.GroupViewSet, basename='groups')

urlpatterns = router.urls + [

]