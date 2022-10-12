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


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `Manufacturer`s to be viewed or edited.
    """
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticated]


class FilamentRollViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `FilamentRoll`s to be viewed or edited.
    """
    queryset = models.FilamentRoll.objects.all()
    serializer_class = serializers.FilamentRollSerializer
    permission_classes = [permissions.IsAuthenticated]


class ModelPrintViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `ModelPrint`s to be viewed or edited.
    """
    queryset = models.ModelPrint.objects.all()
    serializer_class = serializers.ModelPrintSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `groups` to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]