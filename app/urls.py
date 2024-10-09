from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    CarModelViewSet,
    RelationSellModelViewSet,
    SellerModelViewSet,
    OptionViewSet,
    CustomerViewSet,
    CustomAuthToken,
    SellerSaleStatView,
    ConcessionStatView,
)


router = SimpleRouter()
router.register("car_models", CarModelViewSet, basename="car_models")
router.register("relation_sells", RelationSellModelViewSet, basename="relation_sells")
router.register("seller", SellerModelViewSet, basename="seller")
router.register("customer", CustomerViewSet, basename="customer")
router.register("option", OptionViewSet, basename="option")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", CustomAuthToken.as_view()),
    path("stat/seller/<int:seller_id>/", SellerSaleStatView.as_view(), name="seller_stat"),
    path("stat/concession/<int:concession_id>/", ConcessionStatView.as_view(), name="concession_stat"),
]
