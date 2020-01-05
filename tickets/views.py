from datetime import datetime

from django.http import Http404
from django.utils import timezone
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from payments.models import Payment
from tickets.models import Ticket
from tickets.serializers import TicketSerializer
from utils.views import calculate_long_term_park, calculate_payment


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.filter(stage=False)
    authentication_classes = [
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication
    ]
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = [
        'status',
        'admin__username',
        'admin__email'
    ]
    filterset_fields = [
        'admin',
        'ticket_number',
        'vehicle_number',
    ]

    @action(detail=True, methods=['POST'])
    def checkin(self, request, pk=None):
        try:
            ticket = Ticket.objects.get(pk=pk)
            if ticket.slot.status == ticket.slot.FILLED:
                raise ValidationError(detail='Slot is filled')

            ticket.stage = False
            ticket.checkin = timezone.now()
            ticket.save()

            ticket.slot.status = ticket.slot.FILLED
            ticket.slot.save()
            return Response(self.serializer_class(ticket, many=False).data)
        except Ticket.DoesNotExist:
            raise Http404

    @action(detail=True, methods=['POST'])
    def checkout(self, request, pk=None):
        try:
            checkout = timezone.now()
            ticket = Ticket.objects.get(pk=pk)
            ticket.checkout = checkout
            # Calculate payment
            hours = calculate_long_term_park(ticket.checkin, checkout)
            ticket.longtime = hours
            ticket.status = ticket.FINISH
            ticket.save()

            total = calculate_payment(hours)

            # set payment stage
            payment = Payment.objects.get(ticket=ticket)
            payment.stage = False
            payment.total = total
            payment.save()

            ticket.slot.status = ticket.slot.AVAILABLE
            ticket.slot.save()

            return Response(self.serializer_class(ticket, many=False).data)
        except Ticket.DoesNotExist:
            raise Http404

    @action(detail=False, methods=['GET'])
    def unused(self, request):
        queryset = self.filter_queryset(Ticket.objects.filter(stage=True))
        return Response(self.serializer_class(queryset, many=True).data)


    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)

