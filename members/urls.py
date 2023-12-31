"""
This module defines URL patterns for user registration and profile management
using the provided views. It includes URLs for registering a new user,
editing user profiles, changing passwords, displaying user profiles,
editing user profile pages, and creating user profile pages.
"""
from django.urls import path
from .views import (
    UserRegisterView,
    UserEditView,
    PasswordsChangeView,
    ShowProfilePageView,
    EditProfilePageView,
    CreateProfilePageView,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path(
        'password/',
        PasswordsChangeView.as_view(
            template_name='registration/change-password.html'
        ),
        name='password_change'
    ),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(),
         name='show_user_profile_page'),
    path('edit_profile_page/', EditProfilePageView.as_view(),
         name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(),
         name='create_profile_page'),
]
