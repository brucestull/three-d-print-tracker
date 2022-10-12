from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import permissions

from . import serializers

from prints import models


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `users` to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    # queryset = get_user_model().objects.all().order_by('email')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `groups` to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BasicModelPrintViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `ModelPrint`s to be viewed or edited.
    """
    queryset = models.ModelPrint.objects.all()
    serializer_class = serializers.BasicModelPrintSerializer
    permission_classes = [permissions.IsAuthenticated]


class BasicManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `Manufacturer`s to be viewed or edited.
    """
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.BasicManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


# class HyperManufacturerViewSet(viewsets.ModelViewSet):
#     """
#     Test `ViewSet` for `HyperlinkedModelSerializer`.
#     """
#     queryset = models.Manufacturer.objects.all()
#     serializer_class = serializers.HyperManufacturerSerializer
#     permission_classes = [permissions.IsAuthenticated]