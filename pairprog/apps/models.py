from buckets.models import Bucket
from apps.enums import AppTypeEnum
from base.models import TimestampedModel
from django.db import models

# Create your models here.
class App(TimestampedModel):
    name = models.CharField(max_length=250)
    app_type = models.CharField(
        max_length=20,
        choices=AppTypeEnum.choices,
        default=AppTypeEnum.wordpress
    )

    bucket = models.ForeignKey(
        Bucket,
        related_name="apps",
        on_delete=models.CASCADE
    )
