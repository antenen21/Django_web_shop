"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from newsite import settings

from django.contrib.auth import views as auth_views

# Here we actually tell Django that going trough the settings.MEDIA_URL,  which is the path MEDIA_URL = "/media/"  
# it must set the folder "media" as we define it there like:  MEDIA_ROOT = BASE_DIR / "media"  
#  as document_root, so the first place to look for.

urlpatterns = [
    
    path('', include('cart.urls')),
    path('', include('members.urls')),
    path('', include('shop.urls')),
    path('', include('email_management.urls')),
    

    path('', include('django.contrib.auth.urls')), # to use all urls that comes with django from auth
    path('admin/', admin.site.urls),
    

    path('', include('contact.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),
    

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)   
 