from rest_framework.viewsets import GenericViewSet, mixins

from app.constantes import SellerRoles
from app.models import CarModel
from app.serializers import CarModelSerializer
from app.permissions import CarModelPermission
from app.serializers.car_model import PostCarModelSerializer


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
