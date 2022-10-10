# Add Basic Endpoint for `ModelPrint`

## Resources:

## Process:

1. Add a basic serializer class `BasicModelPrintSerializer` for `ModelPrint` in [`api/serializers.py`](../api/serializers.py):
    ```
    class BasicModelPrintSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.ModelPrint
            fields = [
                'id',
                'name',
            ]
    ```

1. Add a basic view class for `ModelPrint` in [`api/views.py`](../api/views.py):
    ```
    class BasicModelPrintViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows `ModelPrints` to be viewed or edited.
        """
        queryset = models.ModelPrint.objects.all()
        serializer_class = BasicModelPrintSerializer
        permission_classes = [permissions.IsAuthenticated]
    ```

1. Add endpoint for `BasicModelPrintViewSet` in [`api/urls.py`](../api/urls.py):
    ```
    #...
    router.register('basic-model-prints', views.BasicModelPrintViewSet, basename='basic_model_prints')
    #...
    ```

1. Test endpoints:
    * http://localhost:8000/api/v1/
    * http://localhost:8000/api/v1/basic-model-prints/

1. Verify knowledge of Django REST API:
    * Attempt, and expect it to fail, adding a `ModelPrint` by providing only the `name` field in the Browsable API:
        ```
        IntegrityError at /api/v1/basic-model-prints/
        NOT NULL constraint failed: prints_modelprint.creator_id
        Request Method:	POST
        Request URL:	http://localhost:8000/api/v1/basic-model-prints/
        Django Version:	4.0
        Exception Type:	IntegrityError
        Exception Value:	
        NOT NULL constraint failed: prints_modelprint.creator_id
        Exception Location:	C:\Users\Bruce\.virtualenvs\three-d-print-tracker-u6Kv-t5s\lib\site-packages\django\db\backends\sqlite3\base.py, line 416, in execute
        Python Executable:	C:\Users\Bruce\.virtualenvs\three-d-print-tracker-u6Kv-t5s\Scripts\python.exe
        Python Version:	3.10.7
        Python Path:	
        ['C:\\Users\\Bruce\\Programming\\three-d-print-tracker',
         'C:\\Users\\Bruce\\Programming',
         'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
         'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
         'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310\\lib',
         'C:\\Users\\Bruce\\AppData\\Local\\Programs\\Python\\Python310',
         'C:\\Users\\Bruce\\.virtualenvs\\three-d-print-tracker-u6Kv-t5s',
         'C:\\Users\\Bruce\\.virtualenvs\\three-d-print-tracker-u6Kv-t5s\\lib\\site-packages']
        Server time:	Mon, 10 Oct 2022 05:20:59 -0400
        ```




1. Proceed to []()

## Repository Links:
* Back to [Add Basic API](./18_add_basic_api.md)
* [README.md](../README.md)