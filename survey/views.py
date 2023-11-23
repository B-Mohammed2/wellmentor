# pylint: disable=E1101
from django.shortcuts import render
from django.views import generic
from profiles.forms import UserProfileForm

# Create your views here.
class SurveyView(generic.View):
  """BASIC VIEW FOR SURVEY PAGE"""

  def get(self, request, *args, **kwargs):
        form = UserProfileForm()
        context = {
            'form': form
        }
        return render(request, "survey/survey.html", context)


class SurveyResultsView(generic.View):
  """BASIC VIEW FOR SURVEY RESULTS PAGE"""

  def get(self, request, *args, **kwargs):
        return render(request, "survey/results.html")


class AboutUsView(generic.View):
  """BASIC VIEW FOR SURVEY RESULTS PAGE"""

  def get(self, request, *args, **kwargs):
        return render(request, "survey/about_us.html")


class HomePageView(generic.View):
  """BASIC VIEW FOR SURVEY PAGE"""

  def get(self, request, *args, **kwargs):
        return render(request, "survey/home.html")
