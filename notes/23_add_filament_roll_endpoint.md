# Add `FilamentRoll` API Endpoint

## Resources:
* [Django REST Framework](https://www.django-rest-framework.org/)

## Process:

1. Create `FilamentRollSerializer` in [`api/serializers.py`](../api/serializers.py):
    ```
    class FilamentRollSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = models.FilamentRoll
            fields = [
                'url',
                'material',
            ]
    ```

1. Create `FilamentRollViewSet` in [`api/views.py`](../api/views.py):
    ```
    class FilamentRollViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows `FilamentRoll`s to be viewed or edited.
        """
        queryset = models.FilamentRoll.objects.all()
        serializer_class = serializers.FilamentRollSerializer
        permission_classes = [permissions.IsAuthenticated]
    ```

1. Create a new `router.register()` for `FilamentRollViewSet` in [`api/urls.py`](../api/urls.py):
    ```
    router.register('filament-rolls', views.FilamentRollViewSet)
    ```

1. Start server and test endpoints:
    1. `python .\manage.py runserver`
    1. Test existing endpoints:
        * http://localhost:8000/api/v1/
        * http://localhost:8000/api/v1/users/
        * http://localhost:8000/api/v1/groups/
        * http://localhost:8000/api/v1/manufacturers/
        * http://localhost:8000/api/v1/model-prints/
    1. Test modified endpoints:
        * http://localhost:8000/api/v1/filament-rolls/
            * http://localhost:8000/api/v1/filament-rolls/1/
            * http://localhost:8000/api/v1/filament-rolls/3/
            * http://localhost:8000/api/v1/filament-rolls/4/

1. `FilamentRoll` endpoints function as expected.

1. Next, add a foreign key field to the serializer.

1. Add `manufacturer` field to `FilamentRollSerializer` in [`api/serializers.py`](../api/serializers.py):
    ```
    class FilamentRollSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = models.FilamentRoll
            fields = [
                'url',
                'material',
                'manufacturer',
            ]
    ```

1. Start server and test endpoints:
    1. `python .\manage.py runserver`
    1. Test modified endpoints:
        * http://localhost:8000/api/v1/filament-rolls/
            * http://localhost:8000/api/v1/filament-rolls/1/
            * http://localhost:8000/api/v1/filament-rolls/3/
            * http://localhost:8000/api/v1/filament-rolls/4/


1. Proceed to []()

## Repository Links:
* Back to [Convert `ModelPrint` endpoint to `HyperlinkedModelSerializer`](./22_convert_model_print_to_hyperlinked.md)
* [README.md](../README.md)