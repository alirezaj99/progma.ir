from django import forms
from .models import Contact
from nocaptcha_recaptcha.fields import NoReCaptchaField


class CreateContactForm(forms.ModelForm):
    captcha = NoReCaptchaField()

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
