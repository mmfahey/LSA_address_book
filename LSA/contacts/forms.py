from django import forms
from django.forms.forms import Form

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['user']

