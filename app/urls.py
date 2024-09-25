from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CarViewSet


router = SimpleRouter()
router.register("car_models", CarViewSet, basename="car_models")

urlpatterns = [
    path("", include(router.urls)),
]
