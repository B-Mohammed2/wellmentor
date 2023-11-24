from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'physical',
            'depression',
            'relationship',
            'professional',
            'mental',
            'anxiety'
        ]