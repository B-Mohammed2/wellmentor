from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'physical_health',
            'depression_level',
            'relationship_health',
            'professional_health',
            'mental_health_awareness',
            'anxiety_level'
        ]