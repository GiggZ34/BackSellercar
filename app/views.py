from django.db import models
from rest_framework.viewsets import GenericViewSet, mixins
from .models import CarModel
from rest_framework.response import Response


class CarViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

