from django_filters import rest_framework as filters
from rest_framework.viewsets import GenericViewSet, mixins
from app.models.customer import Customer

from app.serializers import CustomerSerializer


class CustomerViewSet(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = CustomerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('last_name', 'first_name')

    def get_queryset(self):
        return Customer.objects.all()
