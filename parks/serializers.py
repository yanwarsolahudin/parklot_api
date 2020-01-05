from rest_framework import serializers

from floors.models import Floor
from parks.models import Park
from payments.models import Payment
from payments.serializers import PaymentSerializer


class ParkSerializer(serializers.ModelSerializer):
    is_problem = serializers.SerializerMethodField()


    def get_is_problem(self, value):
        floors = Floor.objects.filter(stage=False, park=value)
        if value.limit_floor < floors.count():
            return True
        return False

    class Meta:
        model = Park
        fields = '__all__'
        read_only_fields = ['admin', 'stage']




