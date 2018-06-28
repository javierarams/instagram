from django import forms
from django.contrib.auth.models import User

from apps.register.models import UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = [
            'is_superuser',
            'is_staff',
            'groups',
            'user_permissions',
            'date_joined',
            'is_active',
            'last_login'
        ]


class RegisterForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['user']
