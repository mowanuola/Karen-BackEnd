import computed_property
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.bmi import calculateBMI
from core.helpers import calculateAge


class User(AbstractUser):
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    sex = models.CharField(blank=True, max_length=50)
    age = computed_property.ComputedIntegerField(
        compute_from='getAge', blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    useractivity = models.IntegerField(blank=True, null=True)
    bmi = computed_property.ComputedIntegerField(
        compute_from='getBMI', blank=True, null=True)
    bloodtype = models.CharField(max_length=50, blank=True, null=True, choices=(
        ("a", "A"),
        ("b", "B"),
        ("ab", "AB"),
        ("o", "O")

    ))
    dci = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def getBMI(self):
        return calculateBMI(self.height, self.weight)

    def getAge(self):
        return calculateAge(self.birth_date)


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
    food = models.ForeignKey(Food, related_name='foods',
                             on_delete=models.CASCADE)
    disease = models.ForeignKey(
        Disease, related_name='diseases', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'User with {} cannot take {}'.format(self.disease, self.food)
