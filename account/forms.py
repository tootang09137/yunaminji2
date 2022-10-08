from django import forms
from django.contrib.auth import forms
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(forms.UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','name','age', 'address','profile_image')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser()
        fields = ('name', 'age', 'address','profile_image')



