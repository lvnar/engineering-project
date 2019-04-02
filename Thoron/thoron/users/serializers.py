from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=255,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_active', 'date_joined')

    def create(self, validated_data):
        password = validated_data.pop('password', '')
        instance = User.objects.create(**validated_data)
        instance.set_password(password)
        instance.save()

        return instance

    def update(self, instance, validated_data):
        for field in validated_data:
            if field != 'password':
                instance.__setattr__(field, validated_data[field])
            else:
                instance.set_password(validated_data[field])
        instance.save()

        return instance
