from django.db import models

from app.constantes import SellerRoles


class Concession(models.Model):
    concession_zip = models.IntegerField(default=0)


class RelationSell(models.Model):
    seller = models.ForeignKey(
        "Seller", on_delete=models.CASCADE, related_name="relations_sells")
    carmodel = models.ForeignKey(
        "CarModel", on_delete=models.CASCADE, related_name="relations_sells")
    customer = models.ForeignKey(
        "Customer", on_delete=models.CASCADE, related_name="relations_sells")
    quantity = models.IntegerField(default=1)


class Seller(models.Model):
    Seller_roles = models.CharField(choices=SellerRoles.choices, max_length=30)
    concession = models.ForeignKey("Concession", on_delete=models.CASCADE)


class CarModel(models.Model):
    Car_model = models.CharField(max_length=200)
    Car_price = models.IntegerField(default=0)
    Car_sell = models.BooleanField(default=False)
    concession = models.ForeignKey("Concession", on_delete=models.CASCADE, related_name="Cars_models")


class Customer(models.Model):
    Customer_name = models.CharField(max_length=200)
