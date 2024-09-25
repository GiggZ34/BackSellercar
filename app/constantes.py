from django.db import models
from django.utils.translation import gettext_lazy as _


class SellerRoles(models.TextChoices):
    STANDARD = "STANDARD", _("Standard")
    OWNER = "OWNER", _("Owner")
