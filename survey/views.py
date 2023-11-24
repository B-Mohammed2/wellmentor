# pylint: disable=E1101
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

# Create your views here.
class SurveyView(generic.View):
  """BASIC VIEW FOR SURVEY PAGE"""
  template_name = 'survey/survey.html'


  def get(self, request, *args, **kwargs):
        form = UserProfileForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

  def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST)
        if form.is_valid():

            form_data = {
                'physical': float(form.cleaned_data['physical']),
                'depression': float(form.cleaned_data['depression']),
                'relationship': float(form.cleaned_data['relationship']),
                'professional': float(form.cleaned_data['professional']),
                'mental': float(form.cleaned_data['mental']),
                'anxiety': float(form.cleaned_data['anxiety']),
            }

            request.session['form_data'] = form_data

            # Perform any additional actions or save the data to the database
            # ...
            if request.user.is_authenticated:
                user_profile = get_object_or_404(UserProfile, user=request.user)
                user_profile.physical = form_data['physical']
                user_profile.depression = form_data['depression']
                user_profile.relationship = form_data['relationship']
                user_profile.professional = form_data['professional']
                user_profile.mental = form_data['mental']
                user_profile.anxiety = form_data['anxiety']
                user_profile.save()

            return redirect(reverse('results'))
        else:
            # Handle the case where the form is not valid
            return render(request, self.template_name, {'form': form})


class SurveyResultsView(generic.View):
    """BASIC VIEW FOR SURVEY RESULTS PAGE"""

    template_name = 'survey/results.html'

    def get(self, request, *args, **kwargs):
        # Retrieve form data from the session
        form_data = request.session.get('form_data', {})

        # Clear form data from the session to avoid displaying it multiple times
        request.session.pop('form_data', None)

        context = {
            'form_data': form_data
        }

        # Otherwise, render the HTML template
        return render(request, self.template_name, context)

class AboutUsView(generic.View):
  """BASIC VIEW FOR SURVEY RESULTS PAGE"""

  def get(self, request, *args, **kwargs):
        return render(request, "survey/about_us.html")


class HomePageView(generic.View):
  """BASIC VIEW FOR SURVEY PAGE"""

  def get(self, request, *args, **kwargs):
        return render(request, "survey/home.html")
