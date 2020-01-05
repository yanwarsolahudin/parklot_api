from rest_framework import serializers

from slots.models import Slot


class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'
        read_only_fields = ['admin', 'stage']


