from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.models import Seller
from app.permissions import SellerPermission
from app.serializers import SellerModelSerializer


class SellerModelViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = SellerModelSerializer
    permission_classes = [SellerPermission]

    def get_queryset(self):
        return Seller.objects.all()
