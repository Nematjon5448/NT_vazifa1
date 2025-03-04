from django import forms
from .models import Comment, Car

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['matni']
        widgets = {
            'matni': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            })
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'nomi': forms.TextInput(attrs={
                "class": 'form-control'
            }),
            'rang': forms.Select(attrs={
                'class': 'form-select'
            }),
            'brand': forms.Select(attrs={
                'class': 'form-select'
            }),
            'ot_kuchi': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'mator_hajmi': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'narx': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'rasm': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
    rasm = forms.ImageField(required=False)