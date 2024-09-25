from rest_framework.viewsets import GenericViewSet, mixins
from app.models import CarModel
from app.serializers import CartModelSerializer
from app.permissions import CarModelPermission


class CarModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = CartModelSerializer
    permission_classes = [CarModelPermission]

    def get_queryset(self):
        return CarModel.objects.all()
