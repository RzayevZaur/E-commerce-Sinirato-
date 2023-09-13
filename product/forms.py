from django import forms
from .models import Review
from django.forms import widgets





class productform(forms.ModelForm):
    class Meta:
        model=Review
        fields=['user','review','Rating_review']
        widgets = {
                'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user'}),
                'review': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'cols': 30, 'style': 'line-height: 1.5rem', 'placeholder': 'review'} ), 
            }




