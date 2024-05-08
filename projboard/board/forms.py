from django import forms
from django.forms import ModelForm
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, Response


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'text', 'author']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # 'text': forms.Textarea(attrs={'class': 'form-control'}),
            'text': forms.CharField(widget=CKEditorUploadingWidget())
        }


class EditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type comment text here ...'}),
        }