from django.contrib.auth.models import AbstractUser
from django.db import models
from app.constantes import SellerRoles


class Concession(models.Model):
    zip = models.IntegerField(default=0)


class RelationSell(models.Model):
    seller = models.ForeignKey(
        "Seller", on_delete=models.CASCADE, related_name="relations_sells"
    )
    carmodel = models.ForeignKey(
        "CarModel", on_delete=models.CASCADE, related_name="relations_sells"
    )
    customer = models.ForeignKey(
        "Customer", on_delete=models.CASCADE, related_name="relations_sells"
    )
    options = models.ManyToManyField("Option", related_name="relations_sells")


class Seller(AbstractUser):
    roles = models.CharField(choices=SellerRoles.choices, max_length=30)
    concession = models.ForeignKey("Concession", on_delete=models.CASCADE)


class CarModel(models.Model):
    model = models.CharField(max_length=200)
    price = models.IntegerField()


class Customer(models.Model):
    Customer_name = models.CharField(max_length=200)


class Option(models.Model):
    model = models.ForeignKey(
        "CarModel", on_delete=models.CASCADE, related_name="Options"
    )
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
