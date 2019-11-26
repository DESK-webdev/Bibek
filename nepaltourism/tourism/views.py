from django.shortcuts import render
from .models import TopPicture,Place,Festival,ToDolist,BlogStory

def home(request):
    pictures = TopPicture.objects.all()
    place = Place.objects.all()
    festival = Festival.objects.all()
    todolist = ToDolist.objects.all()
    blogstory = BlogStory.objects.all()
    return render(request, 'home.html', {'pictures':pictures,'place':place, 'festival':festival, 'todolist':todolist,'blogstory':blogstory  })
