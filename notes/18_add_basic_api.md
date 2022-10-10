# Add Basic API

## Resources:
* Documentation:
    * [Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/#quickstart)
    * [Serializers](https://www.django-rest-framework.org/tutorial/quickstart/#serializers)
    * [GenericAPIView](https://www.django-rest-framework.org/api-guide/generic-views/#genericapiview)
    * [Attributes](https://www.django-rest-framework.org/api-guide/generic-views/#attributes)
    * [`Serializers`](https://www.django-rest-framework.org/api-guide/serializers/#serializers)
    * [`HyperlinkedModelSerializer`](https://www.django-rest-framework.org/api-guide/serializers/#hyperlinkedmodelserializer)
* Related Resources:
    * [`djangorestframework` - pypi.org](https://pypi.org/project/djangorestframework/)

## Process:

1. Install `djangorestframework` Version 3.14.0:
    * `pipenv install djangorestframework==3.14.0`

1. Create `api` app:
    * `python .\manage.py startapp api`

1. Create serializer module [`api/serializers.py`](../api/serializers.py):
    ```
    from django.contrib.auth.models import Group
    from rest_framework import serializers

    from django.contrib.auth import get_user_model


    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = [
                'id',
                'username',
                'email',
            ]


    class GroupSerializer(serializers.ModelSerializer):
        class Meta:
            model = Group
            fields = [
                'id',
                'name',
            ]
    ```

1. Add views to [`api/views.py`](../api/views.py):
    ```
    from django.contrib.auth.models import Group
    from rest_framework import viewsets
    from rest_framework import permissions

    from .serializers import UserSerializer, GroupSerializer
    from django.contrib.auth import get_user_model


    class UserViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows users to be viewed or edited.
        """
        queryset = get_user_model().objects.all().order_by('-date_joined')
        # queryset = get_user_model().objects.all().order_by('email')
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
    urlpatterns = [
        #...
        path('api/v1/', include('api.urls')),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        #...
    ]
    ```

1. Create [`api/urls.py`](../api/urls.py):
    ```
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter

    from . import views


    router = DefaultRouter()
    router.register('users', views.UserViewSet, basename='users')
    router.register('groups', views.GroupViewSet, basename='groups')

    urlpatterns = router.urls + [

    ]
    ```

1. We now have API endpoints for `users` and `groups`.

1. Proceed to [Add Basic Endpoint for `ModelPrint`](./19_add_basic_endpoint_for_model_print.md)

## Repository Links:
* Back to [Fast Forward to Next Thing](./17_fast_forward.md)
* [README.md](../README.md)