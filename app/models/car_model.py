from django.db import models


class CarModel(models.Model):
    model = models.CharField(max_length=200)
    price = models.IntegerField()
