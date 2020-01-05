from django.db import models

from slots.models import Slot
from utils.models import Timestamp, generate_string_code


class Ticket(Timestamp):
    ACTIVE = 'active'
    FINISH = 'finish'
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (FINISH, 'Finish')
    )

    PREFIX = 'PARK'

    slot = models.ForeignKey(Slot, related_name='slottickets', on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=10, unique=True)
    vehicle_number = models.CharField(max_length=10)
    order_date = models.DateField(auto_now_add=True)
    checkin = models.DateTimeField(blank=True, null=True)
    checkout = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)
    admin = models.ForeignKey('auth.User', related_name='admintickets', on_delete=models.CASCADE, blank=True, null=True)
    longtime = models.PositiveIntegerField(default=0)
    stage = models.BooleanField(default=True)

    def __str__(self):
        return self.ticket_number


    def save(self, *args, **kwargs):
        if not self.ticket_number:
            # Newly created object, so set slug
            self.ticket_number = generate_string_code(Ticket)

        super(Ticket, self).save(*args, **kwargs)

