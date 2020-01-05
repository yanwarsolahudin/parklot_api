from django.db import models

from floors.models import Floor
from utils.models import Timestamp


class Slot(Timestamp):
    COMPACT = 'compact'
    LARGE = 'large'
    HANDICAPPED = 'handicapped'
    MOTORCYCLE = 'motorcycle'
    SLOT_TYPE_CHOICES = (
        (COMPACT, 'Compact'),
        (LARGE, 'Large'),
        (HANDICAPPED, 'Handicapped'),
        (MOTORCYCLE, 'Motorcycle'),
    )

    FILLED = 'filled'
    AVAILABLE = 'available'
    STATUS_CHOICES = (
        (FILLED, 'Filled'),
        (AVAILABLE, 'Available'),
    )

    floor = models.ForeignKey(Floor, related_name='floorslots', on_delete=models.CASCADE)
    admin = models.ForeignKey('auth.User', related_name='adminslots', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slot_type = models.CharField(max_length=12, choices=SLOT_TYPE_CHOICES, default=LARGE)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=AVAILABLE)
    stage = models.BooleanField(default=True)

    def __str__(self):
        return self.name



