from django.forms import ModelForm, CharField, Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegistrationForm(UserCreationForm):  
    usable_password = None #to get rid of Password-based authentication:
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter text'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter text'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter text'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),

        }
        
        help_texts= {
            'username':'',
            'is_superuser':'Designates that this user has all permissions without explicitly assigning them.'
        }