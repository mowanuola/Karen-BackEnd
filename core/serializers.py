from core.models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'email', 'password', 'birth_date', 'height', 'weight', 'age', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'calories', 'bloodtype',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at')


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = ('id', 'food', 'disease',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at')


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('id', 'user', 'disease',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at')
