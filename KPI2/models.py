import uuid

from django.db import models

from commsquare.models import Interval


class KPI2(models.Model):
    interval_start_timestamp = models.DateTimeField(blank=True, null=True)
    interval_end_timestamp = models.DateTimeField(blank=True, null=True)
    cell_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    number_of_unique_users = models.IntegerField(default=0)
    interval = models.CharField(
        max_length=2,
        choices=Interval.choices,
        blank=True,
        null=True
    )
