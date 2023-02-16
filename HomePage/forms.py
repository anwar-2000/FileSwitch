from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['username','password']
        labels = {
            "username" : "Your Username",
            "password" : "Your Password"
        }
       
class RegisterForm(UserCreationForm):
   class Meta:
       model = User
       fields =['username','email']