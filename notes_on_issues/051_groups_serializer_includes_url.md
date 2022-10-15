# `Group` List Serializer Includes `url`

## Links:
* [`Group` List Serializer Includes `url`](https://github.com/brucestull/three-d-print-tracker/issues/51)

## Functional Changes:
* [`api/serializers.py`](../api/serializers.py):
    ```
    class GroupSerializer(serializers.HyperlinkedModelSerializer):
        #...
        class Meta:
            #...
            fields = [
                #...
                'url',
                #...
            ]
    ```