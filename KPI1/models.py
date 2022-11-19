import uuid

from django.db import models

from commsquare.models import Interval


class KPI1(models.Model):
    interval_start_timestamp = models.FloatField(blank=True, null=True)#models.DateTimeField(blank=True, null=True)
    interval_end_timestamp = models.FloatField(blank=True, null=True) #models.DateTimeField(blank=True, null=True)
    service_id = models.IntegerField(blank=True, null=True)
    total_bytes = models.IntegerField(default=0)
    interval = models.CharField(
        max_length=10,
        choices=Interval.choices,
        blank=True,
        null=True
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
