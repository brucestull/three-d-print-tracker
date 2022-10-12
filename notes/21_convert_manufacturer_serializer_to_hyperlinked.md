# Convert `Manufacturer` serializer to use `HyperlinkedModelSerializer`

## Resources:
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Quickstart - django-rest-framework.org](https://www.django-rest-framework.org/tutorial/quickstart/#quickstart)

## Process:

1. Change contents and class name of `BasicManufacturerSerializer` to `ManufacturerSerializer` in [`api/serializers.py`](../api/serializers.py):
    ```
    class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = models.Manufacturer
            fields = [
                'url',
                'name',
            ]
    ```

1. Change `router.register()` for `Manufacturer`s in [``](../api/urls.py):
    ```
    router.register('manufacturers', views.ManufacturerViewSet)
    ```

1. Change contents and class name of `BasicManufacturerViewSet` to `ManufacturerViewSet` in [`api/views.py`](../api/views.py):
    ```
    class ManufacturerViewSet(viewsets.ModelViewSet):
        """
        Test `ViewSet` for `HyperlinkedModelSerializer`.
        """
        queryset = models.Manufacturer.objects.all()
        serializer_class = serializers.ManufacturerSerializer
        permission_classes = [permissions.IsAuthenticated]
    ```

1. Start server and test endpoints:
    1. `python .\manage.py runserver`
    1. Test old endpoints:
        * http://localhost:8000/api/v1/
        * http://localhost:8000/api/v1/users/
        * http://localhost:8000/api/v1/groups/
    1. Test modified endpoints:
        * http://localhost:8000/api/v1/manufacturers/
            * http://localhost:8000/api/v1/manufacturers/1/
            * http://localhost:8000/api/v1/manufacturers/2/

1. Endpoints function as needed.

1. Next, change `ModelPrint` endpoint to use `HyperlinkedModelSerializer`.

1. Proceed to []()

## Repository Links:
* Back to [Add Basic `Manufacturer` Endpoint](./20_add_basic_manufacturer_endpoint.md)
* [README.md](../README.md)