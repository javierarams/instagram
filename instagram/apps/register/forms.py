from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from apps.register.models import UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']


class RegisterForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ['user', 'follows', 'follow_requests']

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class EditRegisterForm(UserChangeForm):

    class Meta:
        model = UserProfile
        exclude = ['user', 'follows', 'follow_requests']