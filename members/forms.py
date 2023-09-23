"""
This module imports forms and models related to user authentication,
user creation and modification, password change, and user profiles.
These imports are used for implementing user registration, profile editing,
and password management functionalities.
"""
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    PasswordChangeForm,
)
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from travelblog.models import UserProfile


class ProfilePageForm(forms.ModelForm):
    """
    This form is used to edit user profile information,
    including bio, profile picture, date of birth, website,
    social media profiles, contact details, address, location,
    interests or hobbies, and subscribed categories.
    """
    class Meta:
        """
        This class defines the configuration options for the ProfilePageForm.
        It specifies the model it is based on,
        as well as the fields that should be included in the form
        and their corresponding widgets.
        """
        model = UserProfile
        fields = (
            'bio', 'profile_picture', 'date_of_birth', 'website',
            'facebook_profile', 'twitter_profile', 'linkedin_profile',
            'instagram_profile', 'youtube_profile', 'email',
            'phone_number', 'address', 'location', 'interests_or_hobbies',
            'subscribed_categories'
        )
        
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe yourself here'
            }),
            'profile_picture': forms.FileInput(
                attrs={'class': 'form-control'}
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter website URL here',
            }),
            'facebook_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Facebook profile URL here',
            }),
            'twitter_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Twitter profile URL here',
            }),
            'linkedin_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter LinkedIn profile URL here',
            }),
            'instagram_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Instagram profile URL here',
            }),
            'youtube_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter YouTube profile URL here',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your detailed address here',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your location or city here',
            }),
            'interests_or_hobbies': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your interests or hobbies',
            }),
            'subscribed_categories': forms.CheckboxSelectMultiple(
                attrs={'class': 'form-control'}
            ),
        }


class EditProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'bio', 'profile_picture', 'date_of_birth', 'website',
            'facebook_profile', 'twitter_profile', 'linkedin_profile',
            'instagram_profile', 'youtube_profile', 'email',
            'phone_number', 'address', 'location', 'interests_or_hobbies',
            'subscribed_categories'
        )
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe yourself here'
            }),
            'profile_picture': forms.FileInput(
                attrs={'class': 'form-control'}
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter website URL here',
            }),
            'facebook_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Facebook profile URL here',
            }),
            'twitter_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Twitter profile URL here',
            }),
            'linkedin_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter LinkedIn profile URL here',
            }),
            'instagram_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Instagram profile URL here',
            }),
            'youtube_profile': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter YouTube profile URL here',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your detailed address here',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your location or city here',
            }),
            'interests_or_hobbies': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your interests or hobbies',
            }),
            'subscribed_categories': forms.CheckboxSelectMultiple(),
        }


class SignUpForm(UserCreationForm):
    """
    This form extends the UserCreationForm provided by Django to include
    additional fields for email, first name, and last name.
    It also applies custom widgets to these fields
    to ensure a consistent look and feel.
    """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        """
        This class defines the metadata for the SignUpForm, including the model
        and fields to be displayed in the form.
        """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def __init__(self, *args, **kwargs):
        """
        This extends the UserCreationForm and adds custom
        styling attributes to the 'username', 'password1',
        and 'password2' fields.
        """
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    """
    Custom form for editing user profile information.
    Removes unwanted fields like is_superuser, is_staff, etc.
    """
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'last_login',
            'date_joined'
        )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    date_joined = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
        disabled=True,
    )

    last_login = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
        disabled=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields.pop('is_superuser', None)
        self.fields.pop('is_staff', None)
        self.fields.pop('is_active', None)

        if self.instance:
            self.fields['date_joined'].initial = self.instance.date_joined
            self.fields['last_login'].initial = self.instance.last_login
            self.fields['password'].widget = forms.HiddenInput()
            self.fields['password_change_link'] = forms.CharField(
                widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
                initial=reverse_lazy("password_change")
            )


class PasswordChangedForm(PasswordChangeForm):
    """
    This form extends the PasswordChangeForm provided by Django to include
    custom widgets for password input fields,
    ensuring a consistent look and feel.
    It includes fields for the old password, new password,
    and password confirmation.
    """
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}
        )
    )
    new_password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}
        )
    )
    new_password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}
        )
    )

    class Meta:
        """
        It specifies the model to be used (User) and the fields to be included
        in the form, which are 'old_password',
        'new_password1', and 'new_password2'.
        """
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
