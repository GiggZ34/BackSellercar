from django.contrib.auth.models import AbstractUser
from django.db import models
from app.constantes import SellerRoles


class Seller(AbstractUser):
    roles = models.CharField(choices=SellerRoles.choices, max_length=30)
    concession = models.ForeignKey("Concession", on_delete=models.CASCADE, related_name="sellers", null=True)
