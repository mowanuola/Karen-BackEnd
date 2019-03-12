from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.bmi import calculateBMI


class User(AbstractUser):
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def bmi(self):
        return calculateBMI(self.height, self.weight)


class Food(models.Model):
    name = models.CharField(max_length=50, blank=True)
    calories = models.IntegerField()
    bloodtype = models.CharField(max_length=50, choices=(
        ("a", "A"),
        ("b", "B"),
        ("ab", "AB"),
        ("o", "O")

    ))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Blacklist(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'User with {} cannot take {}'.format(self.disease, self.food)


class Diagnosis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} has {}'.format(self.user.username, self.disease)
