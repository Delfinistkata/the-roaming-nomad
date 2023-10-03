"""
This module contains Django form classes for creating and editing blog content.
These forms are for user interactions in this blog application,
allowing users to create and edit posts,
manage categories, and add comments to posts.
"""
from django import forms
from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    """
    Form for creating and editing blog posts.
    This form class is used to create and edit blog posts.
    It is based on the 'Post' model and includes fields for
    the post's title, title tag, categories, content, featured image,
    excerpt, and status. Additionally, it specifies widget attributes
    for each field to control their appearance in the HTML form.
    This form simplifies the process of creating and editing blog posts
    by providing a user-friendly interface with customizable widgets.
    """
    class Meta:
        """
        This configuration specifies which model fields should be
        included in the form and how they should be presented to users.
        """
        model = Post
        fields = (
            'title',
            'title_tag',
            'categories',
            'body_content',
            'featured_image',
        )

        widgets = {
            'title': forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Fill in your title'
                    }),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'categories': forms.CheckboxSelectMultiple(),
            'body_content': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Text goes here',
                }),
            'featured_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    """
    Form for editing existing blog posts.
    This form class is used to edit existing blog posts.
    It is based on the 'Post' model and includes fields
    for editing the post's title, title tag, categories,
    content, featured image, excerpt, and status.
    Additionally, it specifies widget attributes for each field to control
    their appearance in the HTML form.
    This form simplifies the process of editing existing blog posts
    by providing a user-friendly interface with customizable widgets.
    """
    class Meta:
        """
        This configuration specifies which model fields
        can be edited in the form and how they should be
        presented to users for editing.
        """
        model = Post
        fields = (
            'title',
            'title_tag',
            'categories',
            'body_content',
            'featured_image',
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
        }


class CategoryEditForm(forms.ModelForm):
    """
    Form for editing existing blog categories.
    This form class is used to edit existing blog categories.
    It is based on the 'Category' model
    and includes a field for editing the category name.
    This form simplifies the process of editing existing blog categories
    by providing a user-friendly interface to modify the category name.
    """
    class Meta:
        """
        This configuration specifies which model field
        can be edited in the form and how it should be presented
        to users for editing.
        """
        model = Category
        fields = ['category_name']


class CommentForm(forms.ModelForm):
    """
    Form for creating comments on blog posts.
    This form class is used to create comments on blog posts.
    It is based on the 'Comment' model and includes fields for
    specifying the comment's author and content.
    This form simplifies the process of creating comments on blog posts
    by providing a user-friendly interface to specify the author and content.
    """
    class Meta:
        """
        This configuration specifies which model fields
        should be included in the form and how they should be
        presented to users for creating comments.
        """
        model = Comment
        fields = (
            'body_content',
        )

        widgets = {
            'body_content': forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Comment here',
                }),
        }
