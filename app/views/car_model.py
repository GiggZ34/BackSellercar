from rest_framework.viewsets import GenericViewSet, mixins
from app.models import CarModel
from app.serializers import CarModelSerializer
from app.permissions import CarModelPermission


class CarModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = CarModelSerializer
    permission_classes = [CarModelPermission]

    def get_queryset(self):
        return CarModel.objects.all()
