from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.models import RelationSell

from app.serializers import RelationSellModelSerializer
from app.permissions import RelationSellPermission


class RelationSellModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = RelationSellModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return RelationSell.objects.all()
