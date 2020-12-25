from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'interface', 'timezone')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'interface', 'timezone')

class UserPrefsForm(ModelForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'interface', 'timezone')


