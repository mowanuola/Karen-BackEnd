from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.bmi.views import calculateBMI
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    age = models.IntegerField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def bmi(self):
      return calculateBMI(self.height,self.weight)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Food(models.Model):
    name =  models.CharField(max_length=50, blank=True)  
    calories = models.IntegerField(blank=True)
    bloodtype = models.CharField(max_length=50, blank=True, choices=(
        ("a","A"),
        ("b","B"),
        ("ab","AB"),
        ("o","O")
        
    ))
    def __str__(self):
        return self.name
class Disease(models.Model):
    name = models.CharField(max_length=50, blank=True) 
    def __str__(self):
        return self.name
class Blacklist(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
        
class Diagnosis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    