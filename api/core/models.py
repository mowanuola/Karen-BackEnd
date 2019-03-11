from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self

    # def calculateBMI(self):
      # return self.height * self.weight


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Diagnosis(models.Model):
    def __str__(self):
        return self


class Blacklist(models.Model):
    def __str__(self):
        return self


class Food(models.Model):

    def __str__(self):
        return self


class Disease(models.Model):

    def __str__(self):
        return self
