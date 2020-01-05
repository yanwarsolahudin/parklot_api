from django.db import models

from parks.models import Park
from utils.models import Timestamp


class Floor(Timestamp):
    park = models.ForeignKey(Park, related_name='parkfloors', on_delete=models.CASCADE)
    admin = models.ForeignKey('auth.User', related_name='adminfloor', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    limit_slot = models.PositiveIntegerField(default=1)
    stage = models.BooleanField(default=True)

    def __str__(self):
        return self.name



