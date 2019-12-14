from django.db import models

# Create your models here.

class Clientprofile (models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length = 100, blank = False)
    phone = models.CharField(max_length = 15, blank = False)
    address = models.CharField(max_length = 50, blank=False)

    def __str__(self):
        return self.email
    
class Serviceprovider(models.Model):
    company_name = models.CharField(max_length=50)
    Address = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 15)
    website = models.URLField( max_length=200)
    facebook = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
    Manager = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='serviceproviderimages', height_field=300, width_field=600, max_length=None)

    def __str__(self):
        return self.company_name
    

