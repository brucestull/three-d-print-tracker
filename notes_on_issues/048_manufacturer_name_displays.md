# `Manufacturer` `name` Displayed on `FilamentRoll` List View

## Links:
* [`Manufacturer` `name` displayed on `FilamentRoll` list view.](https://github.com/brucestull/three-d-print-tracker/issues/48)

## Functional Changes:
* [`api/serializers.py`](../api/serializers.py):
    ```
    class FilamentRollSerializer(serializers.HyperlinkedModelSerializer):
        #...
        manufacturer_detail = ManufacturerSerializer(read_only=True, source='manufacturer')
        #...
        class Meta:
            #...
            fields = [
                #...
                'manufacturer_detail',
                #...
            ]
    ```