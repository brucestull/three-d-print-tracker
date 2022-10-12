# Convert `ModelPrint` endpoint to `HyperlinkedModelSerializer`

## Resources:
* [Django REST Framework](https://www.django-rest-framework.org/)

## Process:

1. Change contents and class name `BasicModelPrintSerializer` to `ModelPrintSerializer` in [`api/serializers.py`](../api/serializers.py):
    ```
    class ModelPrintSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = models.ModelPrint
            fields = [
                'url',
                'name',
            ]
    ```

1. Change `BasicModelPrintViewSet` to `ModelPrintViewSet` in [`api/views.py`](../api/views.py):
    ```
    class ModelPrintViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows `ModelPrint`s to be viewed or edited.
        """
        queryset = models.ModelPrint.objects.all()
        serializer_class = serializers.ModelPrintSerializer
        permission_classes = [permissions.IsAuthenticated]
    ```

1. Change `router.register()` from `BasicModelPrintViewSet` to `ModelPrintViewSet` in [`api/urls.py`](../api/urls.py):
    ```
    router.register('model-prints', views.ModelPrintViewSet)
    ```

1. Start server and test endpoints:
    1. `python .\manage.py runserver`
    1. Test existing endpoints:
        * http://localhost:8000/api/v1/
        * http://localhost:8000/api/v1/users/
        * http://localhost:8000/api/v1/groups/
        * http://localhost:8000/api/v1/manufacturers/
    1. Test modified endpoints:
        * http://localhost:8000/api/v1/model-prints/
            * http://localhost:8000/api/v1/model-prints/1/
            * http://localhost:8000/api/v1/model-prints/3/

1. `ModelPrint` endpoints function as expected.

1. Next, add `FilamentRoll` endpoints.

1. Proceed to [Add `FilamentRoll` API Endpoint](./23_add_filament_roll_endpoint.md)

## Repository Links:
* Back to [Convert `Manufacturer` serializer to use `HyperlinkedModelSerializer`](./21_convert_manufacturer_serializer_to_hyperlinked.md)
* [README.md](../README.md)