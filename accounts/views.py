from django.shortcuts import render
from django.urls import reverse_lazy
from accounts.forms import Loginform, Registerform
from django.views.generic import CreateView,FormView,View
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django_email_verification import sendConfirm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView

User=get_user_model()
# Create your views here.
def change_password(request):
    return render(request,'change_password.html')

class CustomLoginView(LoginView):
    template_name='login.html'
    form_class=Loginform
  
    def get_success_url(self):
        return reverse_lazy('core:home')

class RegisterView(CreateView):
    form_class=Registerform
    template_name='register.html'
    success_url='/'
    
    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)
        user = User.objects.get(username=form.cleaned_data['username'],email=form.cleaned_data['email'])
        sendConfirm(user)
        return response

class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('accounts:login')