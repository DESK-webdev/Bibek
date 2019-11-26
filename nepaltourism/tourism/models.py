from django.db import models

class TopPicture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='topimages')

    def __str__(self):
        return self.title


class Place(models.Model):
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='locationimages')
    description = models.TextField()


    def __str__(self):
        return self.location

class Festival(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='festiveimages')
    datetime = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

class ToDolist(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ToDoimages')
    description = models.TextField()

    def __str__(self):
        return self.title

class BlogStory(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Blogimages')
    body = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
