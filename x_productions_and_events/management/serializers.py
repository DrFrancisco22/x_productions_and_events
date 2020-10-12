from rest_framework import serializers
from .models import Events, Visitors

class EventsSerializers(serializers.ModelSerializer):

    date_time = serializers.DateTimeField(format="%Y-%m-%d %I:%M:%p")
    class Meta:
        model = Events
        fields = '__all__'


class VisitorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Visitors
        fields = '__all__'
