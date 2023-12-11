from rest_framework import serializers
from django.contrib.auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    """
    Сериализотор для представления регистрации пользователя.
    """
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        account = User.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password')
        )
        return account

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )
