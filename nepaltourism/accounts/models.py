from django.db import models

# Create your models here.

class profile (models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length = 100, blank = False)
    phone = models.CharField(max_length = 15, blank = False)
    address = models.CharField(max_length = 50, blank=False)

    def __str__(self):
        return self.email

class font(models.Model):
    font_size = models.IntegerField()
