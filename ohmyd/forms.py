from django import forms
from .models import Article

class AForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']