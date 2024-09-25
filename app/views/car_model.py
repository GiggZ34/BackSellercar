from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.models import CarModel

from app.serializers import CartModelSerializer


class CarModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = CartModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return CarModel.objects.all()
