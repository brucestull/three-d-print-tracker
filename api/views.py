from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer
from .serializers import GroupSerializer
from .serializers import BasicModelPrintSerializer

from prints import models


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `users` to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    # queryset = get_user_model().objects.all().order_by('email')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `groups` to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BasicModelPrintViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows `ModelPrints` to be viewed or edited.
    """
    queryset = models.ModelPrint.objects.all()
    serializer_class = BasicModelPrintSerializer
    permission_classes = [permissions.IsAuthenticated]