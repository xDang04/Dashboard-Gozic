from django.forms import ModelForm
from django import forms
from .models import *

class FolderCreateForm(ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Add message ...', 'class': 'p-4 text-black', 'maxlength' : '300', 'autofocus': True }),
        }
class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['name', 'content']
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Add name page', 'class': 'p-4 text-black', 'maxlength' : '300', 'autofocus': True }),
            'content': forms.Textarea(attrs={'class':''})
        }