from django import forms 
from django.forms import ModelForm

from django.contrib.auth.models import User

class UserSignupForm(ModelForm):
    class Meta :
        model = User
        fields = ["username", "password", "email"]
        widgets = {
          'username':forms.TextInput(attrs={
               'class' : 'form-control',
               'style': 'color : #fff'
          }),

          'password': forms.PasswordInput(attrs={
               'class' : 'form-control',
               'style': 'color : #fff'
          }),

          'email' : forms.EmailInput(attrs={
               'class' : 'form-control',
               'style': 'color: #fff'
        })

        }


class UserLoginForm(forms.Form):

     username = forms.CharField(widget=forms.TextInput(attrs={
               'class' : 'form-control',
               'style': 'color : #fff'
          }))

     password = forms.CharField(widget=forms.PasswordInput(attrs={
               'class' : 'form-control',
               'style': 'color : #fff'
          }))
     