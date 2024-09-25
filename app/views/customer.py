from rest_framework.viewsets import GenericViewSet, mixins
from app.models.customer import Customer

from app.serializers import CustomerSerializer

class CustomerViewSet (
GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.all()