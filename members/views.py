from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from travelblog.models import UserProfile
from .forms import SignUpForm, EditProfileForm, PasswordChangedFrom


class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_picture', 'date_of_birth', 'website',
    'facebook_profile', 'twitter_profile',
    'linkedin_profile', 'instagram_profile', 'youtube_profile', 'phone_number', 'address',
    'location', 'interests_or_hobbies', 'subscribed_categories']
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangedFrom
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your password has been changed successfully.')
        return response



class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
