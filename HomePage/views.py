from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .forms import LoginForm


class IndexView(View):
    def get(self,request):
        return render(request,"HomePage/index.html")
    
class LoginView(View):
    def get(self,request):
        context = {"loginform" :  LoginForm() }
        return render(request,"HomePage/login.html",context)
    def post(self,request):
        pass #login logic
