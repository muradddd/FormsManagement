from django import forms
from accounts.models import UserModel
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

User=UserModel
class Registerform(UserCreationForm):#form.Modelforms
    
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'First name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username",'email','image')
  






class Loginform(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    
