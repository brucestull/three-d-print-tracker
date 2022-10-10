# Add Basic API

## Resources:
* [Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/#quickstart)
* [Serializers](https://www.django-rest-framework.org/tutorial/quickstart/#serializers)
* [GenericAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)
* [Attributes](https://www.django-rest-framework.org/api-guide/generic-views/#attributes)
* [`Serializers`](https://www.django-rest-framework.org/api-guide/serializers/#serializers)
* [`HyperlinkedModelSerializer`](https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer)

## Process:

1. Install `djangorestframework`:
    * `pipenv install djangorestframework`

1. Create `api` app:
    * `python .\manage.py startapp api`

1. Create serializer module [`api/serializers.py`](../api/serializers.py):
    ```
    from django.contrib.auth.models import Group
    from rest_framework import serializers

    from accounts.models import CustomUser


    class UserSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = CustomUser
            fields = [
                'url',
                'username',
                'email',
                'groups',
            ]


    class GroupSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Group
            fields = [
                'url',
                'name',
            ]
    ```

1. Add views to [`api/views.py`](../api/views.py):
    ```
    from django.contrib.auth.models import Group
    from rest_framework import viewsets
    from rest_framework import permissions

    from .serializers import UserSerializer, GroupSerializer
    from accounts.models import CustomUser


    class UserViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows users to be viewed or edited.
        """
        queryset = CustomUser.objects.all().order_by('-date_joined')
        serializer_class = UserSerializer
        permission_classes = [permissions.IsAuthenticated]


    class GroupViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows groups to be viewed or edited
        """
        queryset = Group.objects.all()
        serializer_class = GroupSerializer
        permission_classes = [permissions.IsAuthenticated]
    ```

1. Add a few paths to [`print_tracker/urls.py`](../print_tracker/urls.py):
    ```
    #...
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #...
    ```

1. Create [`api/urls.py`](../api/urls.py):
    ```
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter

    from . import views


    router = DefaultRouter()
    router.register('users/', views.UserViewSet, basename='users')
    router.register('groups/', views.GroupViewSet, basename='groups')

    urlpatterns = router.urls + [

    ]
    ```




1. Proceed to []()

## Repository Links:
* Back to [Fast Forward to Next Thing](./17_fast_forward.md)
* [README.md](../README.md)