from django.db import models


class Option(models.Model):
    model = models.ForeignKey(
        "CarModel", on_delete=models.CASCADE, related_name="Options", null=True
    )
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)