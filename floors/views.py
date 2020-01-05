from django.http import Http404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from floors.models import Floor
from floors.serializers import FloorSerializer


class FloorViewSet(viewsets.ModelViewSet):
    serializer_class = FloorSerializer
    queryset = Floor.objects.filter(stage=False)
    authentication_classes = (
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication
    )
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )

    search_fields = [
        'name',
        'admin__username',
        'admin__email',
        'park__name'
    ]

    filterset_fields = ['admin', 'park',]

    @action(detail=False, methods=['GET'])
    def unused(self, request):
        queryset = self.filter_queryset(Floor.objects.filter(stage=True))
        return Response(self.serializer_class(queryset, many=True).data)

    @action(detail=True, methods=['POST'])
    def stage(self, request, pk=None):
        try:
            floor = Floor.objects.get(pk=pk)
            if floor.park.limit_floor < Floor.objects.filter(park=floor.park).count():
                raise ValidationError({'park': ['Limited floor']})

            floor.stage = False
            floor.save()
            return Response(self.serializer_class(floor, many=False).data)
        except Floor.DoesNotExist:
            raise Http404

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)