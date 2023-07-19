from django.db import models





# Create your models here.

class Email(models.Model):
    from_address = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    

    def __str__(self):
        return self.subject
    


   

        