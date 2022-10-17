from django.contrib.auth.models import Group
from rest_framework import serializers

from django.contrib.auth import get_user_model

from prints import models


class NestedUserSerializer(serializers.ModelSerializer):
    """
    Nested serializer for `CustomUser`. Provides 'id', 'username', 'url', and 'is_supermaker' fields.
    """
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'url',
            'is_supermaker',
        ]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `Group`. Provides 'id', 'name', and 'url' fields.
    """
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'url',
        ]


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `Manufacturer`. Provides 'id', 'url', and 'name' fields.
    """
    class Meta:
        model = models.Manufacturer
        fields = [
            'id',
            'name',
            'url',
        ]


class FilamentMaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.FilamentMaterial
        fields = [
            'id',
            'url',
            'polymer_type',
            'METERS_PER_GRAM',
        ]


class FilamentRollSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `FilamentRoll`. Provides 'id', 'material', 'url', 'manufacturer_detail', and 'owner_detail' fields.
    """
    owner_detail = NestedUserSerializer(read_only=True, source='owner')
    manufacturer_detail = ManufacturerSerializer(read_only=True, source='manufacturer')
    class Meta:
        model = models.FilamentRoll
        fields = [
            'id',
            'material',
            'url',
            'manufacturer_detail',
            'owner_detail',
        ]


class NestedFilamentInstanceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Nested serializer for `FilamentInstance`. Provides 'grams_filament_consumed', '__str__' as 'filament_used', and 'url' fields.
    """
    filament_used = serializers.StringRelatedField(source='__str__')
    class Meta:
        model = models.FilamentInstance
        fields = [
            'grams_filament_consumed',
            'filament_used',
            'url',
        ]


class NestedModelPrintSerializer(serializers.HyperlinkedModelSerializer):
    """
    Nested serializer for `ModelPrint`. Provides 'id', 'name', 'url', and 'filament_instance_detail' fields.
    """
    filament_instance_detail = NestedFilamentInstanceSerializer(read_only=True, source='filament_instance')
    class Meta:
        model = models.ModelPrint
        fields = [
            'id',
            'name',
            'url',
            'filament_instance_detail',
        ]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for `CustomUser`. Provides 'id', 'username', 'url', 'email', 'is_supermaker', and 'model_prints_detail' fields.
    """
    model_prints_detail = NestedModelPrintSerializer(many=True, read_only=True, source='prints')
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'url',
            'email',
            'is_supermaker',
            'model_prints_detail',
        ]


class FilamentInstanceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `FilamentInstance`. Provides 'grams_filament_consumed', 'meters_filament_consumed', 'url', 'id', and 'filament_roll_detail' fields.
    """
    filament_roll_detail = FilamentRollSerializer(read_only=True, source='filament_roll')
    class Meta:
        model = models.FilamentInstance
        fields = [
            'grams_filament_consumed',
            'meters_filament_consumed',
            'url',
            'id',
            'filament_roll_detail',
        ]


class ModelPrintSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for `ModelPrint`. Provides 'name', 'id', 'url', 'creator_detail', and 'filament_instance_detail' fields.
    """
    creator_detail = NestedUserSerializer(read_only=True, source='creator')
    filament_instance_detail = FilamentInstanceSerializer(read_only=True, source='filament_instance')
    class Meta:
        model = models.ModelPrint
        fields = [
            'name',
            'id',
            'url',
            'creator_detail',
            'filament_instance_detail',
        ]