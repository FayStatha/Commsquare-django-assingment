from django.db import models


class Interval(models.TextChoices):
    ONE_HOUR = '1-hour'
    FIVE_MINUTE = '5-minutes'
