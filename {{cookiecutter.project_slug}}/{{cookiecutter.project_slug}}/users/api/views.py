# Django
from django.contrib.auth import get_user_model

# Rest
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Serializers
from codebase_django.users.api.serializers import *

User = get_user_model()