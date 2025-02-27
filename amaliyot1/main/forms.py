from django import forms
from .models import Comment

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