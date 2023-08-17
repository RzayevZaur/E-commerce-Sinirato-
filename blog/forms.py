from django import forms
from .models import comment
from django.forms import widgets

class blogforms(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['name', 'email', 'commet', 'Website']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'email' : widgets.EmailInput(attrs={'class': 'form-control required-entry validate-email','placeholder': 'E-mail'} ),
            'commet': widgets.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 30, 'style': 'line-height: 1.5rem', 'placeholder': 'commet'} ),
            'Website':widgets.NumberInput(attrs={'class':'form-control','placeholder': 'Phone'}),
            
        }
