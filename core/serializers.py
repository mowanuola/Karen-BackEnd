from core.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'email', 'birth_date', 'height', 'weight', 'age', 'sex', 'useractivity', 'bmi', 'dci', 'bloodtype', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at')


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('id', 'name', 'calories',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at')


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('id', 'name',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at')


class BlacklistSerializer(serializers.ModelSerializer):
    food = FoodSerializer()
    disease = DiseaseSerializer()

    class Meta:
        model = Blacklist
        fields = ('id', 'food', 'disease',
                  'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at')
