from django.db import models


class Customer(models.Model):
    Customer_name = models.CharField(max_length=200)