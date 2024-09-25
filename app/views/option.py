from rest_framework.viewsets import GenericViewSet, mixins
from app.models.option import Option

from app.serializers import OptionSerializer


class OptionViewSet (
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = OptionSerializer

    def get_queryset(self):
        return Option.objects.all()