from django.db import models
from ckeditor.fields import RichTextField

STATUS = (
    (0,'Draft'),
    (1,"Publish")

)
class TopPicture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='topimages')

    def __str__(self):
        return self.title

class Author(models.Model):
    name =models.CharField(null=False, max_length=50)
    Address = models.CharField(max_length=50)
    Bio = RichTextField()
    image = models.ImageField(upload_to='author-images', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name
class Place(models.Model):
    location = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True,help_text="It will auto-complete automically!",default = '')
    image = models.ImageField(upload_to='locationimages')
    description = RichTextField()


    def __str__(self):
        return self.location

class Festival(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True,help_text="It will auto-complete automically!",default = '')
    image = models.ImageField(upload_to='festiveimages')
    datetime = models.DateTimeField()
    description = RichTextField()

    def __str__(self):
        return self.title

class ToDolist(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True,help_text="It will auto-complete automically!",default = '')
    image = models.ImageField(upload_to='ToDoimages')
    description = RichTextField()

    def __str__(self):
        return self.title

class BlogStory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True,help_text="It will auto-complete automically!", default = '')
    image = models.ImageField(upload_to='Blogimages')
    body = RichTextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default='')
    
    Published_on = models.DateTimeField(auto_now=True)
    Updated_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices = STATUS, default=0)

    class META:
        ordering = ['-Published_on']

    def __str__(self):
        return self.title
