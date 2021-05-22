from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'name')
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 8}
        }
