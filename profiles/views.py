# pylint: disable=E1101
from django.shortcuts import render
from django.views import generic
from .models import UserProfile

# Create your views here.
class HomePageView(generic.ListView):
    model = UserProfile
    template_name = 'profiles/home.html'
    context_object_name = 'user_profiles'

    def get_queryset(self):
        return UserProfile.objects.all()
