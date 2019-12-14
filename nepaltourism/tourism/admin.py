from django.contrib import admin
from .models import *

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display=('location', 'slug',)
    prepopulated_fields = {'slug':('location',)}
admin.site.register(TopPicture)
admin.site.register(Author)
@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display=('title', 'slug',)
    prepopulated_fields = {'slug':('title',)}
@admin.register(ToDolist)
class ToDolistAdmin(admin.ModelAdmin):
    list_display=('title', 'slug',)
    prepopulated_fields = {'slug':('title',)}
@admin.register(BlogStory)
class BlogStoryAdmin(admin.ModelAdmin):
    list_display=('title', 'slug',)
    prepopulated_fields = {'slug':('title',)}
