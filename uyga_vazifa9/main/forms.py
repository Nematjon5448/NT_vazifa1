from django import forms
from .models import Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['matni']
        widgets = {
            'matni': forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            })
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'form2Example1'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'form2Example2'
    }))

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": 'form-control',
        'id': 'form3Example4c'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": 'form-control',
        'id': 'form3Example4cd'
    }))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            "username": forms.TextInput(attrs={
                "class": 'form-control',
                "id": 'form3Example1c'
            }),
            "email": forms.EmailInput(attrs={
                "class": 'form-control',
                'id': 'form3Example3c'
            })
        }