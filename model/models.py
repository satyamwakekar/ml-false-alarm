import django
from django.db import models


# Create your models here.
class Ohlc(models.Model):
    instrument_id = models.FloatField(null=True)
    trade_time_in_min = models.DateTimeField(default=django.utils.timezone.now)
    open = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    close = models.FloatField(null=True)
    indicator = models.CharField(max_length=50, default=None)
    sample_rate = models.IntegerField(null=True)


