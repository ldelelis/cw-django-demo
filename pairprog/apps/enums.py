from django.db import models

class AppTypeEnum(models.TextChoices):
    wordpress = "wordpress"
    magento = "magento"
