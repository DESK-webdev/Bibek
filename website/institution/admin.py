from django.contrib import admin

# Register your models here.

from .models import Booking, Contacted, Aboutus, FacultyStaff, Downloads, Results, Blogs, Courses, social, footer

@admin.register(Booking)
class Bookingadmin(admin.ModelAdmin):
    list_display=('Name','Address','Email','Phone')
@admin.register(Contacted)
class Contactedadmin(admin.ModelAdmin):
    list_display=('Name','Email')

admin.site.register(Aboutus)
admin.site.register(Results)
admin.site.register(Downloads)
admin.site.register(social)
admin.site.register(footer)
@admin.register(Courses)
class Coursesadmin(admin.ModelAdmin):
    list_display=('course',)
@admin.register(Blogs)
class Blogsadmin(admin.ModelAdmin):
    list_display = ('title','slug','Published_on','updated_on')
    list_filter = ('status',)
    search_field = ['title','content']
    prepopulated_field = {'slug',('title',)}
@admin.register(FacultyStaff)
class FacultyStaffadmin(admin.ModelAdmin):
    list_display = ('Name', 'Department', 'Email')
