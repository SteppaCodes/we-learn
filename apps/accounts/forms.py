from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder": "Enter Your first name"})
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={"placeholder":"Enter your last name"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder":"Enter your email"})
    )

    password1= forms.CharField(
        label = "Enter your password",
        widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"})
    )

    password2 = forms.CharField(
        label = "Confirm Pasword",
        widget=forms.PasswordInput(attrs={"placeholder":"Confirm your password"})
    )

    class Meta:
        model= User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder":"enter you email"})
    )

    password= forms.CharField(
        label = "Enter your password",
        widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"})
    )