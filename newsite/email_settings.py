





# Display Gmail Emails in admin pannel over 'email_management' app in admin.py

GMAIL_EMAIL = 'info.antenen@gmail.com'
GMAIL_PASSWORD = 'robert89'





# GMAIL WORKING - getting email to gmail.com from contact form

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'info.antenen@gmail.com'
EMAIL_HOST_PASSWORD = 'nbbszfvdltprhejo'
EMAIL_USE_TLS = True
EMAIL_USE_SLL = False 
 



# Email settings for use  a SMPT in the backend

    # pip install django-smtp-ssl
        # Terminal 1 - python3 manage.py runserver
        # Terminal2 - python3 -m smtpd -n -c DebuggingServer localhost:1025
""" SENDGRID_EMAIL_HOST = "smtp.sendgrid.net"
SENDGRID_EMAIL_PORT = 587
SENDGRID_EMAIL_USERNAME = "info.antenen@gmail.com"
SENDGRID_EMAIL_PASSWORD = "Robert89.bleifrei" """






""" # DUMMY Email settings for showing in the Backend     -> .filebased. <-

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'contact/emails' # stores them in a folder """







# Email settings from mailtrap.io / logged in with info.ant...    <---- Working settings / do not touch!!!!!

""" EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '12e01d1ca56ba8'
EMAIL_HOST_PASSWORD = '6ba11ba20cc954'
EMAIL_PORT = '2525'  """