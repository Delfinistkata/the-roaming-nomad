from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'title_tag',
            'author',
            'categories',
            'body_content',
            'featured_image',
            'excerpt',
            'status',
        )

        widgets = {
            'title': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Fill in your title'
                    }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple,
            'body_content': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Text goes here',
                }),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Text goes here',
                }),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'title_tag',
            'categories',
            'body_content',
            'featured_image',
            'excerpt',
            'status',
        )

        widgets = {
            'title': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Fill in your title'
                    }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple,
            'body_content': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Text goes here',
                }),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Text goes here',
                }),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class CategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']