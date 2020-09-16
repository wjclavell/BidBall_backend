from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, min_length=8, write_only=True)
    # user cannot be allowed to change the jwt token
    token = serializers.CharField(max_length=255, read_only=True)
    balance = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'token', 'balance')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255, read_only=True)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    balance = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'token', 'balance')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to login'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to login'
            )

        user = authenticate(username=username, password=password)  # check for existing user

        if user is None:  # user is not in the db
            raise serializers.ValidationError(
                'A user with that username or password is not found'
            )
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated'
            )

        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "token": user.token,
            "balance": user.balance
        }


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'correct', 'incorrect', 'balance', 'favorite_league', 'favorite_teams')
