
from django.template.loader import render_to_string

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.views.generic.base import TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, EmailMessage  # djangos inbox mail function
from newsite.settings import EMAIL_HOST_USER
from .forms import User


class LoginView(View):

    def get(self, request):
        return render(request, 'members/login.html', {})

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password2']
        user = authenticate(request, username=username, password=password)
        if user is None:
            print("\n {{{{{{{{INFO}}}}}}}} - Login failed \n")
            context = {"error": "Nom d'utilisateur ou Mot de passe invalide."}
            return render(request, 'members/login.html', {})

        print("\n{{{{{{{{INFO}}}}}}}} - User was logged in \n \n")

        login(request, user)
        return redirect('index-path')


class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'members/register.html', {
            "form": form
        })

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('thank-you-path')

        return render(request, 'members/register.html', {
            "form": form
        })


class ThankRegistrationYouView(TemplateView):

    template_name = "members/after-registration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Marcus"
        return context
