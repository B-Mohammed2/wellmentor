from django.urls import path
from . import views

urlpatterns = [
    path('', views.SurveyView.as_view(), name='survey'),
]
