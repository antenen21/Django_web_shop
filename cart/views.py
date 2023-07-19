from typing import Any
from django import http
from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from members.forms import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class CartView(LoginRequiredMixin,TemplateView):
    def dispatch(self, request,*args, **kwargs): # this function dispatches (verteilen) the user in 
                                                 # 2 possibles ways taking arguments like requested user that
                                                 # trys to login.
        if not request.user.is_authenticated:
            return redirect('login-path') # Redirect to your login URL
        

        return super().dispatch(request, *args, **kwargs) # if the user gets here, the function goes up 
                                                          # again with the arguments and dispatches to the other way
                                                          # which would be the next function:  def get()


    def get(self, request, *args, **kwargs):
        return render(request, 'cart/cart.html', {
        })
    
    def post(self,request):
        return None
    
    