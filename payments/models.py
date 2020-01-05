from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from tickets.models import Ticket
from utils.models import Timestamp, generate_string_code


class Payment(Timestamp):
    CREDIT_CARD = 'credit-card'
    CASH = 'cash'
    PAYMENT_TYPE_CHOICES = (
        (CREDIT_CARD, 'Credit Card'),
        (CASH, 'Cash')
    )
    PREFIX = 'PAY'

    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='ticketpayment')
    admin = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='adminpayments')
    payment_number = models.CharField(max_length=10, unique=True)
    payment_type = models.CharField(max_length=12, choices=PAYMENT_TYPE_CHOICES, default=CASH)
    total = models.PositiveIntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    stage = models.BooleanField(default=True)

    def __str__(self):
        return self.payment_number

    def save(self, *args, **kwargs):
        if not self.payment_number:
            # Newly created object, so set slug
            self.payment_number = generate_string_code(Payment)

        super(Payment, self).save(*args, **kwargs)


@receiver(post_save, sender=Ticket)
def create_payment(sender, instance=None, created=False, **kwargs):
    if created:
        Payment.objects.create(ticket=instance, admin=instance.admin, stage=instance.stage)