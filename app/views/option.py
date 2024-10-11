from django.db.models import Q
from django_filters.rest_framework import FilterSet, NumberFilter
from rest_framework.viewsets import GenericViewSet, mixins
from app.models.option import Option

from app.serializers import OptionSerializer
from app.permissions import OptionPermission


class OptionFilterSet(FilterSet):
    vehicle_model = NumberFilter(method="filter_vehicle_model")

    class Meta:
        model = Option
        fields = ['vehicle_model']

    def filter_vehicle_model(self, queryset, name, value):
        return queryset.filter(Q(model_id=value) | Q(model__isnull=True))


class OptionViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = OptionSerializer
    filterset_class = OptionFilterSet
    permission_classes = [OptionPermission]


    def get_queryset(self):
        return Option.objects.all()
