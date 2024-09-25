from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CarModelViewSet
from .views import CustomerViewSet
from .views import OptionViewSet

router = SimpleRouter()
router.register("car_models", CarModelViewSet, basename="car_models")
router.register("customer", CustomerViewSet, basename="customer")
router.register("option", OptionViewSet, basename="option")

urlpatterns = [
    path("", include(router.urls)),
]
