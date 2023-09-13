from django import forms
from .models import User

from django.contrib.auth.forms import (
UserCreationForm, 
AuthenticationForm, 
PasswordResetForm,
SetPasswordForm
)




class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Your Password'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Your Confirm Password'}))
                                                            
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Your First Name"}),

            'last_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': "Your Last Name"}),

            'email': forms.EmailInput(attrs={'class': 'form-control',
                                            'placeholder': "Your Email Address"}),
          
        }



    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Password and confirm password doesn't match")
        return password2



class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control', 
            'placeholder': 'Your Email'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input-text',
            'placeholder': 'Your Password'
        }))
        
