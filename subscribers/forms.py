from django import forms
from .models import Subscribe
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class SubscribeForm(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        # self.fields['active'] = True

    class Meta:
        model = Subscribe
        fields = ['email']
