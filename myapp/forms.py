# forms.py
from django import forms
from .models import *

class HotelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
    from_email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'placeholder':'Your Email'}))
    subject = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField( widget=forms.Textarea(attrs={'placeholder': 'Message'}) , required=True)
