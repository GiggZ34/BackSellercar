from django.db import models


class Concession(models.Model):
    zip = models.IntegerField(default=0)
