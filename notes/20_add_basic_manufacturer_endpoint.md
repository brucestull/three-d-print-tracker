# Add Basic `Manufacturer` Endpoint

## Resources:
* [Django REST Framework](https://www.django-rest-framework.org/)
* [Quickstart - django-rest-framework.org](https://www.django-rest-framework.org/tutorial/quickstart/#quickstart)

## Process:

1. Add basic serializer class `BasicManufacturerSerializer` for `Manufacturer` to [`api/serializers.py`](../api/serializers.py):
    ```
    class BasicManufacturerSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Manufacturer
            fields = [
                'id',
                'name',
            ]
    ```

1. Add basic view class `BasicManufacturerViewSet` for `Manufacturer` to [`api/views.py`](../api/views.py):
    ```
    class BasicManufacturerViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows `Manufacturer`s to be viewed or edited.
        """
        queryset = models.Manufacturer.objects.all()
        serializer_class = serializers.BasicManufacturerSerializer
        permission_classes = [permissions.IsAuthenticated]
    ```

1. Add endpoint for `BasicManufacturerViewSet` in [`api/urls.py`](../api/urls.py):
    ```
    router.register('basic-manufacturers', views.BasicManufacturerViewSet)
    ```

1. Test endpoints:
    * http://localhost:8000/api/v1/
    * http://localhost:8000/api/v1/basic-manufacturers/

1. Proceed to [Convert `Manufacturer` serializer to use `HyperlinkedModelSerializer`](./21_convert_manufacturer_serializer_to_hyperlinked.md)

## Repository Links:
* Back to [Add Basic Endpoint for `ModelPrint`](./19_add_basic_endpoint_for_model_print.md)
* [README.md](../README.md)