from django import forms
from .models import Category, Comment


class BookForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-select'
    }))
    publication_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date'
    }))
    isbn = forms.CharField(max_length=13, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    genre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    summary = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3
    }))
    views = forms.IntegerField(initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            })
        }
        labels = {
            'text': 'Matni'
        }