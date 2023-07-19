


        ██████╗ ███████╗ █████╗ ██████╗ ███╗   ███╗███████╗
        ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝
        ██████╔╝█████╗  ███████║██║  ██║██╔████╔██║█████╗  
        ██╔══██╗██╔══╝  ██╔══██║██║  ██║██║╚██╔╝██║██╔══╝  
        ██║  ██║███████╗██║  ██║██████╔╝██║ ╚═╝ ██║███████╗
        ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚══════╝ ANTENEN 
▄███▓▒░ SHIFT + CMD + P   - ASCII Decorator    ░▒▓█████▓▒░ ░▒▓████████████████▄                                     
 ██                                                                          ██
 ██                                                                          ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░

┌─────────────────────────────────────────────────────────────────────────────┐
│AGAiNST THE COMERCiALiSATiON OF THE COMPUTERSCENE·REMEMBER!·DO IT JUST 4 FUN!│
└─────────────────────────────────────────────────────────────────────────────┘



     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ TERMINAL - COMMANDS ░▒███████████████████████████████████████████████▄                                     
 ██                                                                          ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░
            MAIN COMMANDS FOR THE TERMINAL

         cd FolderName				         
         cd ..					               
         cd ~		                        [OPTION + N] = [~]	
         ls					                  
         pwd					               
         mkdir FolderName			        
         Rm -r FolderName  		         
         python3 -m venv env			                                       
         source env/bin/activate	
         python3 manage.py runserver	                                                  
         python3 -m pip install django		 												
         django-admin startproject CarRent	
         django-admin startapp LoginApp	             


         superuser

         for pythonanywhere:
         python3 manage.py collectstatic
         pip3 freeze > requirements.txt
         compress everything of your folder and name it code.zip

         in bash console of pythonanywhere unzip the uploaded file code.zip with:
         unzip code.zip
 ░                                                                            ░
 ░░                                                                          ░░
 ▒▒                                                                          ▒▒
 ▓▓                                                                          ▓▓
 ██                                                                          ██
 ▀████████████████████████████████████████████████████████████████████████████▀






    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ FAVICON ░▒▓██████████████████████████████████████████████████████████▄                                     
 ██                                                                          ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░                                  
        1.pip install django-favicon                    

        2. add 'favicon',  to apps in settings.py

        3.Create a static folder in the project-level directory

            ├── django_project
            │   ├── __init__.py
            |   ├── asgi.py
            │   ├── settings.py
            │   ├── urls.py
            │   └── wsgi.py
            ├── manage.py
            ├── static  # new
            │   ├── images

        4. add in urls.py main project :   path('', include('favicon.urls')),

        5. add in it your logo/icon named as favicon.png                                                                                  
 ░                                                                            ░
 ░░                                                                          ░░
 ▒▒                                                                          ▒▒
 ▓▓                                                                          ▓▓
 ██                                                                          ██
 ▀████████████████████████████████████████████████████████████████████████████▀







    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ DJANGO EMAIL FUNCTION ░▒▓████████████████████████████████████████████▄                                     
 ██                  youtube: code with stein - reset password               ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
       1. in settings.py write down the variables:


       EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
       EMAIL_FILE_PATH = BASE_DIR / 'emails'
 ░                                                                            ░
 ░░                                                                          ░░
 ▒▒                                                                          ▒▒
 ▓▓                                                                          ▓▓
 ██                                                                          ██
 ▀████████████████████████████████████████████████████████████████████████████▀








    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ IMAGES EXAMPLES ░▒▓██████████████████████████████████████████████████▄                                     
 ██                                                                          ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░
         in HTML                                                                      
        <img src="{% static 'shop/images/background.png' %}


        in CSS files
        background-image: url('/static/shop/images/background_house.png');
 ░                                                                            ░
 ░░                                                                          ░░
 ▒▒                                                                          ▒▒
 ▓▓                                                                          ▓▓
 ██                                                                          ██
 ▀████████████████████████████████████████████████████████████████████████████▀







     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ LOGIN - ACCES TO A CERTAIN PAGE ░▒███████████████████████████████████▄                                     
 ██                                                                          ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░
         for having access to a certain page only loged in we import in
         the views.py:

            from django.contrib.auth.mixins import LoginRequiredMixin

         and use it like this:   

            class CartView(LoginRequiredMixin,TemplateView):

               def get(self, request, *args, **kwargs):
               return render(request, 'cart/cart.html', {
               })
               def post(self,request):
               return None
 ░                                                                            ░
 ░░                                                                          ░░
 ▒▒                                                                          ▒▒
 ▓▓                                                                          ▓▓
 ██                                                                          ██
 ▀████████████████████████████████████████████████████████████████████████████▀









     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ COVERAGE - UNUSED CODE ░▒████████████████████████████████████████████▄                                     
 ██                                                                          ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░
            Here are the general steps to use Coverage.py:
               pip install coverage

            Run your tests with coverage enabled:
               coverage run manage.py test

            Generate a coverage report:
               coverage report
 ░                                                                            ░
 ░░                                                                          ░░
 ▒▒                                                                          ▒▒
 ▓▓                                                                          ▓▓
 ██                                                                          ██
 ▀████████████████████████████████████████████████████████████████████████████▀






     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ EMAIL - SEND EMAIL ░▒████████████████████████████████████████████████▄                                     
 ██                                                                          ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░
   SMTP (Simple Mail Transfer Protocol)

   is a TCP/IP protocol used in sending and receiving email.
   SMTP is used most commonly by email clients, including Gmail, Outlook, Apple Mail and Yahoo Mail.
   SMTP can send and receive email,
   but email clients typically use a program with SMTP for sending email.



      ///views.py///                                                            
      import in views:
         from django.core.mail import send_mail
         


      ///html///
      write the forms direct in the html file WITHOUT using forms.py

          <div class="form-group">
                                <input type="text" class="form-control" id="name" name="name" placeholder="Nom" required="" autofocus="">
                            </div>
                        
                        
                            <div class="form-group form_left">
                                <input type="email" class="form-control" id="email" name="email" placeholder="Email" required="">
                            </div>
                        

      ///views.py///
      fetch data from the forms in de views.py
     

   def Contact(request):
      if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        phone = request.POST['phone']

        print('the form was valid')




        # use the imported send_mail():

        send_mail(
            name,  # title
            content,  # content
            email,  # sender
            ['andreasantenen89@gmail.com', 'info.antenen@gmail.com'],# to email / reciver
            fail_silently=False,
        )

        return redirect('contact-path')

      else: 
         return render(request, 'contact/contact.html', {
                  })


   /// settings.py ///

   # Email settings for showing in the Backend as DUMMY
      EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
      EMAIL_FILE_PATH = BASE_DIR / 'contact/emails' # stores them in a folder


   ###### UNTIL HERE WE GET THE EMAILS IN OUR FOLDER ###############

      now we want pass all that data in a html file:
         in the folder emails create a html document like this:
         ├── contact
         │  ├── emails
            │   ├──contactform.html

      
   in the views.py in our function we want to pass this data so we do that under the fetched data
   like that:

         from django.template.loader import render_to_string


         html = render_to_string('contact/emails/contactform.html', {
            'name' : name,
            'email': email,
            'content' : content,
            'phone' : phone,
        })

   after that we have to specifiy it below also in the send_mail() at the end like that:
         send_mail(
            name,  # title
            content,  # content
            email,  # sender
            ['andreasantenen89@gmail.com', 'info.antenen@gmail.com'],# to email / reciver
            fail_silently=False,
            html_message=html, # here we point at the html file from above
        )

        -with that we basicaly just send the created html file
        -we still nid to pass the data like always in the html file with 
         {{ name }}
         from above --->            html = render_to_string('contact/emails/contactform.html', {
                                          "name" : name
                                             })
         
         in the contactform.html we use now the django tags {{name}} and so on like:
            <h2>Contact form submission</h2>
               <p><b>Name:</b> {{ name }}</p>
               <p><b>Email:</b> {{ email }}</p>
               <p><b>Content:</b> {{ content }}</p>
               <p><b>phone:</b> {{ phone }}</p>


         now we will use the SMTP from gmail to get emails on our gmail account:

            - go in your email account
               - manage your account
                  - security
                     - enable 2 factor verification
                        - go under app passwords (try in the searchbar if you can't find it)
                           -create a new app and it will give you a passworde which you put under the EMAIL_HOST_PASSWORD

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Always the same
EMAIL_HOST = 'smtp.gmail.com'                                  # Always the same
EMAIL_PORT = 587                                               # Always the same          
EMAIL_HOST_USER = 'info.antenen@gmail.com'                     # Where emails should go!
EMAIL_HOST_PASSWORD = 'nbbszfvdltprhejo'                       # <--- created password from google account
EMAIL_USE_TLS = True
EMAIL_USE_SLL = False

    
      -------------------------------------------------------------------------------
      # DUMMY Email settings for showing in the Backend     -> .filebased. <-
      EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
      EMAIL_FILE_PATH = BASE_DIR / 'contact/emails' # stores them in a folder """

 ░                                                                                           ░
 ░░                                                                                         ░░
 ▒▒                                                                                         ▒▒
 ▓▓                                                                                         ▓▓
 ██                                                                                         ██
 ▀███████████████████████████████████████████████████████████████████████████████████████████▀





     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ JAZZMIN - ADMIN PAGE ░▒██████████████████████████████████████████████▄                                     
 ██     https://django-jazzmin.readthedocs.io/installation/                  ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░
               Installation¶

            Install the latest pypi release with pip install -U django-jazzmin

            Add jazzmin to your INSTALLED_APPS before django.contrib.admin, and Voila!

            INSTALLED_APPS = [
               'jazzmin',

               'django.contrib.admin',
               [...]
            ]

      Create next to the settings.py a file named jazzmin.py for example.
         inside write down all the settings to not poluate the settings.py file
            in the settings.py file import it with "from .jazzmin import JAZZMIN_SETTINGS
               then in settings.py at the end tell django that the imported settings are the 
               JAZZMIN_SETTINGS like that:
               
                 JAZZMIN_SETTINGS = JAZZMIN_SETTINGS 

       Now an ERROR will raise with the language_set, in the jazzmin settings
        at the end we delete or comment out this settings:
         "language_chooser": True,          
 ░                                                                            ░
 ░░                                                                          ░░
 ▒▒                                                                          ▒▒
 ▓▓                                                                          ▓▓
 ██                                                                          ██
 ▀████████████████████████████████████████████████████████████████████████████▀




     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ ADMIN - DISPLAY IMAGES IN PRODUCTS   ░▒██████████████████████████████▄                                     
 ██                                                                          ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░
   
   # in template you can use {{ object.description|truncatewords:50 }} for short description  
      in models.py:
         under each models:

         class Product(models.Model):
            category = models.ForeignKey(Category, on_delete=models.CASCADE)
            name = models.CharField(max_length=100)
            description = models.TextField()
            price = models.DecimalField(max_digits=10, decimal_places=2)
            image = models.ImageField(upload_to='product_images/')

            
            <-------- admin_photo
            @property
            def short_description(self):
               return truncatechars(self.description, 20)

            def admin_photo(self):
               return mark_safe('<img src="{}" width="100" />'.format(self.img.url))
            admin_photo.short_description = 'Image'
            admin_photo.allow_tags = True
            <-------- admin_photo

            def __str__(self):
               return self.name



       under admin.py:        <-------- admin_photo

         class ProductAdmin(admin.ModelAdmin):
            list_display = ('name', 'category', 'price', "img", 'admin_photo',)
            list_filter = ('category',)
            search_fields = ('name',)        
 ░                                                                            ░
 ░░                                                                          ░░
 ▒▒                                                                          ▒▒
 ▓▓                                                                          ▓▓
 ██                                                                          ██
 ▀████████████████████████████████████████████████████████████████████████████▀



     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
 ▄███▓▒░ EXAMPLE - EXAMPLE  ░▒████████████████████████████████████████████████▄                                     
 ██                                                                          ██
 ▓█                                                                          █▓
 ▓▓                                                                          ▓▓
 ▒▒                                                                          ▒▒
 ░░                                                                          ░░
 ░                                                                            ░
   
            COPY THIS - DO NOT CHANGE

 ░                                                                            ░
 ░░                                                                          ░░
 ▒▒                                                                          ▒▒
 ▓▓                                                                          ▓▓
 ██                                                                          ██
 ▀████████████████████████████████████████████████████████████████████████████▀
