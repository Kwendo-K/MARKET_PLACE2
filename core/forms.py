from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "username", "class": "form-control px-2 py-2"}
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.widgets.PasswordInput(
            attrs={"placeholder": "password", "class": "form-control px-2 py-2"}
        ),
    )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "username", "class": "form-control px-2 py-2"}
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "example@gmail.com",
                "class": "form-control px-2 py-2",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.widgets.PasswordInput(
            attrs={"placeholder": "", "class": "form-control px-2 py-2"}
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.widgets.PasswordInput(
            attrs={"placeholder": "", "class": "form-control px-2 py-2"}
        ),
    )

