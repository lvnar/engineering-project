from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'number_plate', 'last_position', 'owner')
    

    def validate_last_position(self, value):
        for coord in value:
            if coord > 180 or coord < -180:
                raise serializers.ValidationError(
                    'Coordenadas inválidas.'
                )
        return value

