from django import forms
from django.core.exceptions import ValidationError

from .models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['password1'].required = True
        self.fields['password2'].required = True

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 7:
            raise ValidationError('نام کاربری باید حداقل 7 کارکتر باشد')
        return super(CreateUserForm, self).clean_username()
