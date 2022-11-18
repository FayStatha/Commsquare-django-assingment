from django.db import models

from commsquare.models import Interval


class KPI1(models.Model):
    interval_start_timestamp = models.DateTimeField(blank=True, null=True)
    interval_end_timestamp = models.DateTimeField(blank=True, null=True)
    service_id = models.AutoField(primary_key=True, default=0)
    total_bytes = models.IntegerField(default=0)
    interval = models.CharField(
        max_length=2,
        choices=Interval.choices,
        blank=True,
        null=True
    )
