from django.db import models


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
