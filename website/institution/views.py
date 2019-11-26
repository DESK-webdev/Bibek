from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .forms import Contactedform, Bookingforms
from .models import Contacted, Courses,Booking,Results,Downloads,Aboutus, FacultyStaff,Blogs
# Create your views here.

def home(request):
    download = Downloads.objects.all()
    result = Results.objects.all()
    aboutus = Aboutus.objects.all()
    blog = Blogs.objects.all()
    return render(request, 'home.html',{'download':download,'result':result,'blog':blog,'aboutus':aboutus})
def contact(request):
    if request.method == 'POST':
        form = Contactedform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact') # does nothing, just trigger the validation
    else:
            form = Contactedform()
    return render(request, 'contact.html', {'form': form})
def bookings(request):
    if request.method =='POST':
        form= Bookingforms(request.POST)
        if form.is_valid:
            form.save()
            return redirect('book-now/')
    else:
            form = Bookingforms
    return render(request,'book-seat.html',{'form':form})

def downloads(request):
    download = Downloads.objects.all()
    return render(request,'downloads.html',{'download':download})

def results(request):
    result = Results.objects.all()
    return render(request, 'results.html',{'result':result})

def aboutus(request):
    about = Aboutus.objects.all()
    return render(request,'aboutus.html',{'about':about})

def blogs(request):
    blog = Blogs.objects.all()
    return render(request, 'blogs.html',{'blog':blog})
def facultystaff(request):
    faculty = FacultyStaff.objects.all()
    for i in range( 10):
        a = i
    return render(request,'faculty.html', {'faculty':faculty}, {'a':a})