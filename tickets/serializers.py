from rest_framework import serializers

from payments.models import Payment
from payments.serializers import PaymentSerializer
from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['admin', 'stage', 'ticket_number']

    payment = serializers.SerializerMethodField()

    def get_payment(self, value):
        try:
            payment = Payment.objects.get(ticket=value)
            return PaymentSerializer(payment, many=False).data
        except:
            return {}