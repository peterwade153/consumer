from django.db import models
from django.contrib.gis.db.models import PointField


class Consumer(models.Model):
    consumer_id = models.IntegerField(unique=True)
    street = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    previous_jobs_count = models.IntegerField()
    amount_due = models.IntegerField()
    geometry = PointField()

    def __str__(self):
        return self.consumer_id
