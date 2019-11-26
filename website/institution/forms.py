from django import forms
from django.shortcuts import render, redirect
from .models import Contacted, Booking

class Contactedform(forms.ModelForm):
    class Meta:
        model = Contacted
        widgets = {
            'Name':forms.TextInput(attrs={'placeholder':'Name'}),
            'Email':forms.TextInput(attrs={'placeholder':'E-mail'}),
            'Subject':forms.TextInput(attrs={'placeholder':'Subject'}),
            'Message':forms.Textarea(attrs={'placeholder':'Your Message'})
        }
        fields = ('Name','Email', 'Subject','Message')

class Bookingforms(forms.ModelForm):
    class Meta:
        model = Booking
        widgets = {
            'Name':forms.TextInput(attrs={'placeholder':'Name'}),
            'Email':forms.TextInput(attrs={'placeholder':'E-mail'}),
            'Address':forms.TextInput(attrs={'placeholder':'Address'}),
            'College':forms.Textarea(attrs={'placeholder':'Your College'}),
            'Photo':forms.ImageField(),
            'GPA':forms.TextInput(attrs={'placeholder':'E-mail'}),
            'Guardain_name':forms.TextInput(attrs={'placeholder':'Guardain Name'}),
            'DOB':forms.Textarea(attrs={'placeholder':'Date Of Birth'}),
            'Phone':forms.TextInput(attrs={'placeholder':'Phone Number'})
        }
        fields = ('Name','Email', 'Address','College','Photo','GPA'
        ,'Guardain_name','DOB','Phone')