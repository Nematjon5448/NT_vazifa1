from django import forms
from .models import Brand

class BrandForm(forms.Form):
    nomi = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": 'form-control'
    }))
    davlati = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "form-control"
    }))

class CarForm(forms.Form):
    model = forms.CharField(max_length=80, widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    ot_kuchi = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control"
    }))
    rangi = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    narxi = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "form-control"
    }))
    rasmi = forms.ImageField(required=False ,widget=forms.FileInput(attrs={
        "class": "form-control"
    }))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select(attrs={
        "class": "form-select"
    }))