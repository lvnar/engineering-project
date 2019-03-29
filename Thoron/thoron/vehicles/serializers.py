from rest_framework import serializers
from django.contrib.auth.models import User
from thoron.users.serializers import UserSerializer
from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):

    owner_id = serializers.PrimaryKeyRelatedField(
        required=False,
        write_only=True,
        queryset=User.objects.all(),
        source='owner'
    )
    owner = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Vehicle
        fields = ('id', 'number_plate', 'last_position', 'owner_id', 'owner', 'date_joined')
    

    def validate_last_position(self, value):
        for coord in value:
            if coord > 180 or coord < -180:
                raise serializers.ValidationError(
                    'Coordenadas inválidas.'
                )
        return value

    def get_owner(self, obj):
        return UserSerializer(obj.owner).data

