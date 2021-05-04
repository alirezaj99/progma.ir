from django import forms
from .models import Subscribe


class SubscribeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        # self.fields['active'] = True

    class Meta:
        model = Subscribe
        fields = ['email']
