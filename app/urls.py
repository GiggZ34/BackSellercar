from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    CarModelViewSet,
    RelationSellModelViewSet,
    SellerModelViewSet,
    OptionViewSet,
    CustomerViewSet,
    CustomAuthToken,
    GeneralStatView,
    SellerSaleStatViewSet,
    ConcessionStatViewSet
)


router = SimpleRouter()
router.register("car_models", CarModelViewSet, basename="car_models")
router.register("relation_sells", RelationSellModelViewSet, basename="relation_sells")
router.register("seller", SellerModelViewSet, basename="seller")
router.register("customer", CustomerViewSet, basename="customer")
router.register("option", OptionViewSet, basename="option")

# stat
router.register("stat_seller", SellerSaleStatViewSet, basename="stat_seller")
router.register("stat_concession", ConcessionStatViewSet, basename="stat_concession")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", CustomAuthToken.as_view()),
    path("stat_general/", GeneralStatView.as_view())
]
