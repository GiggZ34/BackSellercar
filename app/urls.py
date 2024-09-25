from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CarModelViewSet


router = SimpleRouter()
router.register("car_models", CarModelViewSet, basename="car_models")

urlpatterns = [
    path("", include(router.urls)),
]
