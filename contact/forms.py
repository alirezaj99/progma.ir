from django import forms
from .models import Contact
from captcha.fields import ReCaptchaField, ReCaptchaV2Checkbox
from captcha.widgets import ReCaptchaV2Checkbox


class CreateContactForm(forms.ModelForm):
    captcha = ReCaptchaField(
        label='اعتبار سنجی',
        widget=ReCaptchaV2Checkbox(
            api_params={
                'hl': 'fa'
            }
        ),
        error_messages={
            'required': 'لطفا اعتبار سنجی رو انجام بدید.',
        }
    )

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
