from django.db import models

from utils.models import Timestamp


class Park(Timestamp):
    admin = models.ForeignKey('auth.User', related_name='adminparks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    limit_floor = models.PositiveIntegerField(default=1)
    stage = models.BooleanField(default=True)

    def __str__(self):
        return self.name


