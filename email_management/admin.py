
from django.contrib import admin
from django.shortcuts import render, HttpResponse
from requests import request
from .models import Email
from . import views



class EmailAdmin(admin.ModelAdmin):
    
    list_filter = ('subject', 'from_address')
    search_fields = ('subject',)

    
    """ action = views.fetch_emails(request)
    HttpResponse('admin/email-management/email-result/') """


 


admin.site.register(Email, EmailAdmin)
