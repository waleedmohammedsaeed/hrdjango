from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass  # Use Django's built-in AuthenticationForm

class PasswordChangeCustomForm(PasswordChangeForm):
    pass  # Use Django's built-in PasswordChangeForm

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
