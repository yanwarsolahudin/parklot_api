from rest_framework import serializers

from floors.models import Floor


class FloorSerializer(serializers.ModelSerializer):
    is_problem = serializers.SerializerMethodField()

    def get_is_problem(self, value):
        if value.park.stage:
            return True
        return False

    class Meta:
        model = Floor
        fields = '__all__'
        read_only_fields = ['admin', 'stage']



