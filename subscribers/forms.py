from django import forms
from .models import Subscribe
from captcha.fields import ReCaptchaField


class SubscribeForm(forms.ModelForm):
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        # self.fields['active'] = True

    class Meta:
        model = Subscribe
        fields = ['email']
