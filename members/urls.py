from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login-page', views.LoginView.as_view(), name='login-path'), 
    path('logout-page', auth_views.LogoutView.as_view(template_name='members/logout.html'), name='logout-path'),
    path('thank-you', views.ThankRegistrationYouView.as_view(), name="thank-you-path"),
    path('register', views.RegisterView.as_view(), name="register-path"), # as_view() is needed to tell django
                                                                        # to use the methods from the class 
]
