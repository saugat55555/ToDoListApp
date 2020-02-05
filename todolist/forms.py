from django import forms
from .models import Lists

class Form(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ['task', 'done']