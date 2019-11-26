from django.db import models
from ckeditor.fields import RichTextField

STATUS = (
    (0,'Draft'),
    (1,'Publish')
)
# Create your models here.

class Booking(models.Model):
    Name = models.CharField(max_length=255, blank=False)
    Email = models.EmailField(blank =False)
    Phone = models.CharField(max_length=12,blank=False)
    Guardain_name = models.CharField(max_length=255,blank=False)
    Address = models.CharField(max_length=255, blank=False)
    Photo = models.ImageField(upload_to='newregisteredimages/')
    DOB = models.DateField(auto_now=False, blank=False)
    College = models.CharField(max_length = 255,blank= False)
    GPA = models.FloatField(blank=False)

    def __str__(self):
        return self.Name

class Contacted(models.Model):
    Name = models.CharField(max_length=255, blank=False)
    Email = models.EmailField(blank =False)
    Subject = models.CharField(max_length=255)
    Message  = RichTextField(blank=False)

    def __str__(self):
        return self.Name


class Aboutus(models.Model):
    Introduction = RichTextField(blank=False)
    Facilities = RichTextField(blank =False)
    def __str__(self):
        return self.Introduction
class FacultyStaff (models.Model):
    Name = models.CharField(max_length=255, blank = False,help_text="Name of the staff")
    Image = models.ImageField(upload_to='images/faculty_staff',help_text="Image of the staff",default='')
    Department = models.CharField(max_length=255, blank=False)
    Email = models.EmailField(blank = False)

    def __str__(self):
        return self.Name
class Blogs(models.Model):
    title = models.CharField(max_length=255, help_text="Enter title")
    slug = models.SlugField(max_length=255, unique=True,help_text="It will auto-complete automically!")
    image = models.ImageField(upload_to='images/blogs',help_text="enter feature image of post",default='')
    content =RichTextField()
    Published_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    status= models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-Published_on']
    def __str__(self):
        return self.title

class Results(models.Model):
    result = models.FileField(help_text="Upload file")
    date = models.DateTimeField(auto_now=True)

class Downloads(models.Model):
    downloads = models.FileField(help_text="upload file")
    date = models.DateTimeField(auto_now=True)
class Courses(models.Model):
    course = models.CharField(blank=False, max_length=255)
    detail = RichTextField()
    image = models.ImageField(upload_to ='images/course',default='')

class social(models.Model):
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length = 255, default= '')

class footer(models.Model):
    faq = RichTextField()
    career = RichTextField()
    privacy = RichTextField()
