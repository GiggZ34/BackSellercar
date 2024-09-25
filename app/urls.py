from django.urls import path
from .views import CarViewSet


urlpatterns = [
    path("get-all-cars/", CarViewSet.as_view(), name="all-car"),
]
