from django import forms
from .models import Contact


class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
