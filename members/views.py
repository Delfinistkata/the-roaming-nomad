"""
This module contains various imports and view classes
for the travelblog application.
It includes imports for rendering templates, working with generic views,
changing passwords, and handling user profiles. Additionally, it imports forms
used for user registration, profile editing, and password change operations.
"""
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from travelblog.models import UserProfile
from travelblog.models import Post
from .forms import (
    SignUpForm,
    EditProfileForm,
    PasswordChangedForm,
    ProfilePageForm,
)


class CreateProfilePageView(CreateView):
    """
    This class-based view handles the creation of a user profile page.
    It uses the UserProfile model and the ProfilePageForm to allow users to
    fill in their profile information, and associates the profile with the
    currently logged-in user.
    """
    model = UserProfile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        """
        Handle a valid form submission.
        This method is called when the submitted form data is valid.
        It associates the user profile with the currently logged-in user.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    """
    This class-based view allows users to edit their profile information.
    It uses the UserProfile model and specifies the fields that can be edited.
    After successful editing, users are redirected to the home page.
    """
    model = UserProfile
    template_name = 'registration/edit_profile_page.html'
    fields = [
        'bio', 'profile_picture', 'date_of_birth', 'website',
        'facebook_profile', 'twitter_profile',
        'linkedin_profile', 'instagram_profile', 'youtube_profile',
        'phone_number', 'address', 'location',
        'interests_or_hobbies', 'subscribed_categories'
    ]
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    """
    This class-based view allows users to view
    the profile page of a specific user.
    It retrieves information about the user and
    their posts to display on the profile page.
    """
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        """
        This method retrieves information about the user and their posts
        to provide context data for rendering the profile page.
        """
        context = super().get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        user_posts = Post.objects.filter(author=page_user.user)

        context['page_user'] = page_user
        context['user_posts'] = user_posts
        return context


class PasswordsChangeView(PasswordChangeView):
    """
    This class-based view allows users to change their passwords.
    It uses the PasswordChangedForm and specifies the URL to redirect to
    upon successful password change.
    """
    form_class = PasswordChangedForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        This method is called when the submitted form data is valid.
        It displays a success message upon successful password change.
        """
        response = super().form_valid(form)
        messages.success(
            self.request,
            'Your password has been changed successfully.'
        )

        return response


class UserRegisterView(generic.CreateView):
    """
    This class-based view allows new users to register on the platform.
    It uses the SignUpForm for registration and specifies the template for
    the registration page as well as
    the URL to redirect to upon successful registration.
    """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    """
    This class-based view allows users to edit their profile information.
    It uses the EditProfileForm for editing and specifies the template for
    the profile editing page as well as
    the URL to redirect to upon successful editing.
    """
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        """
        This method overrides the get_object method to return the instance of
        the currently authenticated user for editing.
        """
        return self.request.user
