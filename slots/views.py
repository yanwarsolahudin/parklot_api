from django.http import Http404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from slots.models import Slot
from slots.serializers import SlotSerializer


class SlotViewSet(viewsets.ModelViewSet):
    serializer_class = SlotSerializer
    queryset = Slot.objects.filter(stage=False)
    authentication_classes = (
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication
    )
    permission_classes = (IsAuthenticatedOrReadOnly, )
    search_fields = [
        'name',
        'admin__username',
        'admin__email',
        'floor__name',
        'floor__id',
        'floor__park__name',
        'floor__park__id',
    ]
    filterset_fields = ['admin', 'floor', 'status']

    @action(detail=True, methods=['POST'])
    def stage(self, request, pk=None):
        try:
            slot = Slot.objects.get(pk=pk)
            if slot.floor.limit_slot < Slot.objects.filter(floor=slot.floor).count():
                raise ValidationError({'slot': ['Limited floor']})

            slot.stage = False
            slot.save()
            return Response(self.serializer_class(slot, many=False).data)
        except Slot.DoesNotExist:
            raise Http404

    @action(detail=False, methods=['GET'])
    def unused(self, request):
        queryset = self.filter_queryset(Slot.objects.filter(stage=True))
        return Response(self.serializer_class(queryset, many=True).data)

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)