from django.contrib import admin
from .models import *
from django.contrib.auth.models import *
# Register your models here.
admin.site.site_header = 'Nepal Tourism Board'
@admin.register(profile)
class profileadmiin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','phone','address')
    list_display_links  = ('email',)
    list_editable = ('first_name', 'last_name')
    list_filter = ('email',)
    search_fields = ('first_name',)
admin.site.unregister(Group)
admin.site.register(font)
