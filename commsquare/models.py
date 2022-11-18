from django.db import models
from django.utils.translation import gettext_lazy as _


class Interval(models.TextChoices):
    ONE_HOUR = '1H', _('1-hour')
    FIVE_MINUTE = '5M', _('5-minute')
