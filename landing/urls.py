from django.urls import path
from . import views

urlpatterns = [
    path('', views.LandingView.as_view(), name='landing-path'),
    path('test', views.TestView.as_view(), name='landing-path'),
]