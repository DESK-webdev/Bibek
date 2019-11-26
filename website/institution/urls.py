from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from website import settings
urlpatterns = [
    path('',views.home, name='site-home'),
    path('contact/',views.contact,name='contact'),
    path('results/',views.results,name='results'),
    path('downloads/',views.downloads,name='downloads'),
    path('bookings/',views.bookings, name='booking'),
    path('blogs/',views.blogs,name='blogs'),
    path('faculty-staff/',views.facultystaff,name='faculty'),
    path('about-us/',views.aboutus,name='aboutus'),
    
    
]