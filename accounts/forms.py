from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class signUpForm(UserCreationForm):
    email = forms.CharField(max_length=50,widget=forms.EmailInput,required=True)

    class Meta:
        model = User
        fields = ['email','username','password1','password2','first_name','last_name']
