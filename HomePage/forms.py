from django import forms
from .models import User


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields ="__all__"
        exclude = ["username"]
        labels = {
            "email" : "Your Email",
            "password" : "Your Password"
        }
       
class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields="__all__"
        labels={
            "username" : "Your Username",
            "email":"Your Email",
            "password" : "Your Password"
        }