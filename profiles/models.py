# pylint: disable=E1101

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class UserProfile(models.Model):

    """USER MODEL FOR SIGNED UP USERS, THIS EXTENDS THE ALL AUTH USER AND ADDS PROFILE INFO"""

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    physical_health = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    social_health = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    professional_health = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    emotional_health = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])


    def __str__(self):
        return str(self.user)

    def calculate_physical_health(self):
        calculated_value = 10 * 10
        self.physical_health = calculated_value
        self.save()
        return calculated_value

    def calculate_social_health(self):
        calculated_value = 10 * 10
        self.social_health = calculated_value
        self.save()
        calculated_value = 10 * 10
        return calculated_value

    def calculate_professional_health(self):
        calculated_value = 10 * 10
        self.professional_health = calculated_value
        self.save()

        return calculated_value

    def calculate_emotional_health(self):
        calculated_value = 10 * 10
        self.emotional_health = calculated_value
        self.save()
        return calculated_value



def create_user_profile(instance, created, *args, **kwargs):
    """
    Signal handler function to create a user profile when a
    new user is created.

    This function is connected to the User model's post_save signal.
    kwargs are required for dispatch signals

    """
    if created:
        UserProfile.objects.create(user=instance)

# Connects profile to user instance with signals
models.signals.post_save.connect(create_user_profile, sender=User)
