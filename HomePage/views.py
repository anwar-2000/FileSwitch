from django.shortcuts import render ,redirect
from django.urls import reverse 
from django.http import HttpResponseRedirect 


from django.contrib import messages
from django.contrib.auth import login , authenticate , logout

from django.views.generic import View
# Create your views here.
from .forms import RegisterForm


class IndexView(View):
    def get(self,request):
        return render(request,"HomePage/index.html")
    
    #logout
def logout(request):
    logout(request)
    return redirect('loginPage')


class LoginView(View):

    def get(self,request):
        return render(request,"HomePage/login.html")

    def post(self,request):
           username = request.POST['username']
           password = request.POST['password']
           print(username,password)#works
           user = authenticate(request,username=username,password=password)
           print('user : ',user)#none -> it works now
           
           if user is not None:
               login(request,user)
               return redirect('homepage')
           else:
                messages.info(request,'Email or Password are incorrect')
                return render(request,"HomePage/login.html") 
       

class RegisterView(View):
    
    def get(self,request):
        context = {"registerform" :  RegisterForm() }
        return render(request,"HomePage/signUp.html",context)
    

    def post(self,request):
       form = RegisterForm(request.POST)
       if form.is_valid():
           form.save()
           user = form.cleaned_data.get('username')
           messages.success(request,'Account succesfully created for ' + user)
           return HttpResponseRedirect(reverse('loginPage'))
       else:
           context = {"registerform" : form}
           return render(request,"HomePage/signUp.html",context) 

