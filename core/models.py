import computed_property
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.bmi import calculate_bmi
from core.helpers import calculate_age


class User(AbstractUser):
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    sex = models.CharField(max_length=50)
    age = computed_property.ComputedIntegerField(
        compute_from='get_age', null=True)
    birth_date = models.DateField(null=True)
    useractivity = models.IntegerField(null=True)
    bmi = computed_property.ComputedIntegerField(
        compute_from='get_bmi', null=True)
    bloodtype = models.CharField(max_length=50, null=True, choices=(
        ("a", "A"),
        ("b", "B"),
        ("ab", "AB"),
        ("o", "O")

    ))
    dci = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def get_bmi(self):
        return calculate_bmi(self.height, self.weight)

    def get_age(self):
        return calculate_age(self.birth_date)


class Food(models.Model):
    img = models.TextField(blank=True) 
    name = models.CharField(max_length=50)
    calories = models.IntegerField()
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
