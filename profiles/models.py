# pylint: disable=E1101

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class UserProfile(models.Model):

    """USER MODEL FOR SIGNED UP USERS, THIS EXTENDS THE ALL AUTH USER AND ADDS PROFILE INFO"""

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    physical = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    depression = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    relationship = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    professional = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    mental = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    anxiety = models.DecimalField(
        max_digits=5, decimal_places=2, default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])


    def __str__(self):
        return str(self.user)

    def calculate_physical_level(self):
        calculated_value = 10 * 10
        self.physical = calculated_value
        self.save()
        return calculated_value

    def calculate_depression_level(self):
        calculated_value = 10 * 10
        self.depression = calculated_value
        self.save()
        return calculated_value

    def calculate_relationship_level(self):
        calculated_value = 10 * 10
        self.relationship = calculated_value
        self.save()
        return calculated_value

    def calculate_professional_level(self):
        calculated_value = 10 * 10
        self.professional = calculated_value
        self.save()

        return calculated_value

    def calculate_mental_level(self):
        calculated_value = 10 * 10
        self.mental = calculated_value
        self.save()

        return calculated_value

    def calculate_anxiety_level(self):
        calculated_value = 10 * 10
        self.anxiety = calculated_value
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
