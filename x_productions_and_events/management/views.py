from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Events, Visitors
from .serializers import EventsSerializers, VisitorsSerializers

class EventsViewset(viewsets.ModelViewSet):
    queryset = Events.objects.select_related()
    serializer_class = EventsSerializers

class VisitorsViewset(viewsets.ModelViewSet):
    queryset = Visitors.objects.select_related()
    serializer_class = VisitorsSerializers

class GetVisitors(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        queryset = Events.objects.get(pk = pk).visitors_set.all()
        serializer = VisitorsSerializers(queryset, many=True)
        return Response(serializer.data)
