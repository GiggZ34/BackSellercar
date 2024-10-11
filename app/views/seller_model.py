from rest_framework.viewsets import GenericViewSet, mixins
from app.models import Seller
from app.permissions import SellerPermission
from app.serializers import SellerModelSerializer
from app.constantes import SellerRoles


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

        user: Seller = self.request.user

        if user.is_anonymous:
            return Seller.objects.none()

        query_role_mapped = {
            SellerRoles.ELON: Seller.objects.all(),
            SellerRoles.OWNER: Seller.objects.all(),
            SellerRoles.STANDARD: Seller.objects.filter(concession_id=user.concession),
        }

        return query_role_mapped[user.roles]

    def get_serializer_class(self):
        return SellerModelSerializer


