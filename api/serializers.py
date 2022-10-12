from django.contrib.auth.models import Group
from rest_framework import serializers

from django.contrib.auth import get_user_model

from prints import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'email',
        ]


class NestedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
        ]


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Manufacturer
        fields = [
            'url',
            'name',
        ]


class FilamentRollSerializer(serializers.HyperlinkedModelSerializer):
    owner_detail = NestedUserSerializer(read_only=True, source='owner')
    class Meta:
        model = models.FilamentRoll
        fields = [
            'url',
            'material',
            'manufacturer',
            'owner_detail',
        ]


class ModelPrintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ModelPrint
        fields = [
            'url',
            'name',
        ]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
        ]