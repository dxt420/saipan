from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from . models import *

from django.forms import ModelChoiceField,ModelForm,TextInput,Textarea

from django.db import transaction

from django.utils.translation import ugettext_lazy as _
import datetime




class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'}))
    last_name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'}))
    phone = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','autocomplete':'off'})) 
    password1 = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','type' : 'password',}))   
    password2 = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control','type' : 'password',}))  
    pin1 = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))   
    pin2 = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'form-control'}))  


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name','last_name','email','username','phone')
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = "Email Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Re-Type Password"
    

    # @transaction.atomic    
    # def save(self):        
    #     user = super().save(commit=False)
    #     user.save()    
                
    #     return user