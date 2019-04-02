from rest_framework import serializers
from django.contrib.auth.models import User
from thoron.users.serializers import UserSerializer
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):

    owner_id = serializers.PrimaryKeyRelatedField(
        required=False,
        queryset=User.objects.all(),
        source='owner'
    )

    class Meta:
        model = Vehicle
        fields = (
            'id',
            'number_plate',
            'last_position',
            'owner_id',
            'is_active',
            'date_joined'
        )
    

    def validate_last_position(self, value):
        for coord in value:
            if coord > 180 or coord < -180:
                raise serializers.ValidationError(
                    'Coordenadas inválidas.'
                )
        return value
    
    def validate_owner(self, value):
        if value is not None and value.is_active == False:
            raise serializers.ValidationError(
                'Propietario inactivo.'
            )
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_superuser == False:
            validated_data['owner'] = user
        if 'owner' not in validated_data or \
            validated_data['owner'].is_active == False:
            raise serializers.ValidationError(
                'Propietario inactivo o no proporcionado.'
            )
        return super().create(validated_data)
    def update(self, instance, validated_data):
        if instance.is_active != True:
            validated_data = {}
        return super().update(instance, validated_data)

