# pylint: disable=E1101
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import UserProfile

# Create your views here.


class HomePageView(LoginRequiredMixin, generic.DetailView):
    """BASIC VIEW FOR LISING ALL THE USER PROFILES ON THE ROOT PAGE"""
    model = UserProfile
    template_name = 'profiles/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        user = UserProfile.objects.get(user=self.request.user)
        return user
