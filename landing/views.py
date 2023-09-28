from django.shortcuts import render
from django.views import View
# Create your views here.

class LandingView(View):

    def get(self, request):
        return render(request, 'landing/landing.html', {})



class TestView(View):

    def get(self, request):
        return render(request, 'landing/test.html', {})