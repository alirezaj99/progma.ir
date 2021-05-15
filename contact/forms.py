from django import forms
from .models import Contact
from captcha.fields import ReCaptchaField


class CreateContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
