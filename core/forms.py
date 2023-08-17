from django import forms
from .models import Contactinfo
from django.forms import widgets
class contactforms(forms.ModelForm):
    class Meta:
        model = Contactinfo
        fields = '__all__'
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'Email' : widgets.EmailInput(attrs={'class': 'form-control required-entry validate-email','placeholder': 'E-mail'} ),
            'Message': widgets.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 30, 'style': 'line-height: 1.5rem', 'placeholder': 'Messenger'} ),
            'Phone':widgets.NumberInput(attrs={'class':'form-control','placeholder': 'Phone'}),
            'Subject':widgets.TextInput(attrs={'class':'form-control','placeholder': 'Subject'})
        }
