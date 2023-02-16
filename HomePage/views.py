from django.shortcuts import render 
from django.urls import reverse
from django.http import HttpResponseRedirect 

from django.contrib.auth import login , authenticate

from django.views.generic import View
# Create your views here.
from .forms import LoginForm , RegisterForm


class IndexView(View):
    def get(self,request):
        return render(request,"HomePage/index.html")
    
class LoginView(View):


    def get(self,request):
        context = {"loginform" :  LoginForm() }
        return render(request,"HomePage/login.html",context)
    

    def post(self,request):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            email = loginform.cleaned_data['email']
            password = loginform.cleaned_data['password']
            user = authenticate(request,username=email,password=password)
            if user is not None:
                #i'll add session logic here
                login(request,user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                context = {"loginform" : loginform}
                return render(request,"HomePage/login.html",context)
        else :
            context = {"loginform" :  LoginForm() }
            return render(request,"HomePage/login.html",context)

class RegisterView(View):

    def get(self,request):
        context = {"registerform" :  RegisterForm() }
        return render(request,"HomePage/signUp.html",context)
    

    def post(self,request):
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            #email = registerform.cleaned_data['email']
            #password = registerform.cleaned_data['password']
            new_user = registerform.save(commit=False)
            new_user.email= registerform.cleaned_data['email']
            new_user.set_password(registerform.cleaned_data['password'])
            new_user.save()

            user = authenticate(request,username=new_user.email,password=registerform.cleaned_data['password'])
            if user is not None:
                #i'll add session logic here
                login(request,user)
                return HttpResponseRedirect(reverse('homepage'))
        else:
            context ={ "registerform" : registerform}
            return render(request,"HomePage/signUp.html",context)

