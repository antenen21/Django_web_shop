from django.shortcuts import render, redirect
from django.template.loader import render_to_string



from django.http import HttpResponseRedirect

from django.views import View
from django.views.generic.base import TemplateView

from django.core.mail import send_mail
from newsite.settings import EMAIL_HOST_USER







# Create your views here.


def Contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        phone = request.POST['phone']

        # pass data in a html document ------ specify this html document below in the send_mail function
        html = render_to_string('contact/emails/contactform.html', {
            'name' : name,
            'email': email,
            'content' : content,
            'phone' : phone,
        })

        # SEND EMAIL FROM DJANGO'S ORIGINALS EMAIL FUNCTION
        send_mail(
            name,  # title
            content,  # content
            email,  # sender
            ['info.antenen@gmail.com',],# to email / reciver
          #                         """ fail_silently=False, """  
            html_message=html, # here we point at the html file from above
        )
        
        return redirect('contact-path')

    else: 
        return render(request, 'contact/contact.html', {
            
                })



