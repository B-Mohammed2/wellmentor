# pylint: disable=E1101
from django.shortcuts import render
from django.views import generic

# Create your views here.
class SurveyView(generic.View):

  def get(self, request, *args, **kwargs):
        return render(request, "survey/survey.html")


class SurveyResultsView(generic.View):

  def get(self, request, *args, **kwargs):
        return render(request, "survey/results.html")
