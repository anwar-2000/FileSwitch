from django.urls import path
from . import views 

urlpatterns = [
    path("",views.IndexView.as_view(),name="homepage"),
    path("login",views.LoginView.as_view(),name="loginPage"),
    path("signUp",views.RegisterView.as_view(),name="registerPage")
]
