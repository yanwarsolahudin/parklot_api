from django.http import Http404
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from parks.models import Park
from parks.serializers import ParkSerializer


class ParkViewSet(viewsets.ModelViewSet):
    serializer_class = ParkSerializer
    queryset = Park.objects.filter(stage=False)
    authentication_classes = (
        TokenAuthentication,
        BasicAuthentication,
        SessionAuthentication,
    )
    permission_classes = (IsAuthenticatedOrReadOnly,)

    search_fields = ['name', 'admin__username', 'admin__email']
    filterset_fields = ['admin',]

    @action(detail=True, methods=['POST'])
    def stage(self, request, pk=None):
        try:
            park = Park.objects.get(pk=pk)
            park.stage = False
            park.save()
            return Response(self.serializer_class(park, many=False).data)
        except Park.DoesNotExist as e:
            raise Http404


    @action(detail=False, methods=['GET'])
    def unused(self, request):
        queryset = self.filter_queryset(Park.objects.filter(stage=True))
        return Response(self.serializer_class(queryset, many=True).data)

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)

