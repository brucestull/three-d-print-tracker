from django.contrib.auth.models import Group
from rest_framework import serializers

from django.contrib.auth import get_user_model

from prints import models


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for `CustomUser`. Provides 'username', 'email', and 'is_supermaker' fields.
    """
    class Meta:
        model = get_user_model()
        fields = [
            'url',
            'username',
            'email',
            'is_supermaker',
        ]


class NestedUserSerializer(serializers.ModelSerializer):
    """
    Serializer for `CustomUser`. Provides 'username', and 'is_supermaker' fields.
    """
    class Meta:
        model = get_user_model()
        fields = [
            'url',
            'username',
            'is_supermaker',
        ]


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `Manufacturer`. Provides 'name' field.
    """
    class Meta:
        model = models.Manufacturer
        fields = [
            'url',
            'name',
        ]


class FilamentRollSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `FilamentRoll`. Provides `material`, `manufacturer`, and `owner_detail` fields.
    """
    owner_detail = NestedUserSerializer(read_only=True, source='owner')
    manufacturer_detail = ManufacturerSerializer(read_only=True, source='manufacturer')
    class Meta:
        model = models.FilamentRoll
        fields = [
            'url',
            'material',
            'manufacturer_detail',
            'owner_detail',
        ]


class ModelPrintSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `ModelPrint`. Provides `name`, and `creator_detail` fields.
    """
    creator_detail = NestedUserSerializer(read_only=True, source='creator')
    class Meta:
        model = models.ModelPrint
        fields = [
            'url',
            'name',
            'creator_detail',
        ]


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for `Group`. Provides `name` field.
    """
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
        ]