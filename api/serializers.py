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


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `Group`. Provides `name` field.
    """
    class Meta:
        model = Group
        fields = [
            'url',
            'name',
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


class FilamentInstanceSerializer(serializers.HyperlinkedModelSerializer):
    filament_roll_detail = FilamentRollSerializer(read_only=True, source='filament_roll')
    class Meta:
        model = models.FilamentInstance
        fields = [
            'url',
            'filament_consumed',
            'filament_roll_detail',
        ]


class ModelPrintSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `ModelPrint`. Provides `name`, and `creator_detail` fields.
    """
    creator_detail = NestedUserSerializer(read_only=True, source='creator')
    filament_instance_detail = FilamentInstanceSerializer(read_only=True, source='filament_instance')
    class Meta:
        model = models.ModelPrint
        fields = [
            'url',
            'name',
            'creator_detail',
            'filament_instance_detail',
        ]