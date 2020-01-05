from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.filter(stage=False)
    authentication_classes = (
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication
    )
    permission_classes = (IsAuthenticatedOrReadOnly,)
    search_fields = [
        'admin__username',
        'admin__email',
        'payment_number',
    ]
    filterset_fields = [
        'admin',
        'payment_number'
    ]


    @action(methods=['POST'], detail=True)
    def cash(self, request, pk=None):
        payment = self.get_object()
        payment.payment_type = payment.CASH
        payment.is_paid = True
        payment.save()

        return Response(self.serializer_class(payment, many=False).data)

    @action(methods=['POST'], detail=True)
    def cc(self, request, pk=None):
        payment = self.get_object()
        payment.payment_type = payment.CREDIT_CARD
        payment.is_paid = True
        payment.save()

        return Response(self.serializer_class(payment, many=False).data)