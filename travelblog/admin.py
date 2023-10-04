"""
Admin configuration for the travel blog application.

This module contains the admin configuration for the travel blog application.
It defines the admin classes for the Post, Category, and Comment models, along
with their respective configurations such as list displays, search fields,
and actions.

Additionally, it imports the necessary modules and models required for the
admin configuration.
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment, UserProfile


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model.

    This class defines the admin configuration for the Post model.
    It specifies the list display fields, search fields, list filters,
    prepopulated fields, and Summernote fields for rich text editing.
    """
    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'body_content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body_content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model.

    This class defines the admin configuration for the Comment model.
    It specifies the list display fields, list filters, search fields,
    actions, and additional methods for managing comments.
    """
    list_display = ('author', 'body_content', 'post', 'date_posted',
                    'approved')
    list_filter = ('approved', 'date_posted')
    search_fields = ('author', 'email', 'body_content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Action method for approving selected comments.
        This method is invoked when the admin user selects the action
        to approve one or more comments. It updates the 'approved' field
        of the selected comments to True, indicating that they are approved.
        """
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    This class defines the admin configuration for the Category model.
    It specifies the list display fields and defines a custom method
    to display the count of associated posts for each category.
    """
    list_display = ('category_name', 'post_count',)

    def post_count(self, obj):
        """
        Method to display the count of associated posts
        for each category.
        """
        return obj.post_set.count()

    post_count.short_description = 'Post Count'


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    This class defines the admin configuration for the UserProfile model.
    It specifies the list display fields, list filter options, search fields,
    and fieldsets for organizing user profile information, including personal
    information, social media links, contact details, and interests.
    """
    list_display = ['user', 'profile_picture', 'date_of_birth', 'location']
    list_filter = ['location', 'subscribed_categories']
    search_fields = ['user__username', 'user__email', 'location']
    fieldsets = (
        (None, {'fields': ('user', 'profile_picture')}),
        ('Personal Information', {
            'fields': ('bio', 'date_of_birth', 'location', 'address')
        }),
        ('Social Media', {
            'fields': (
                'website', 'facebook_profile', 'twitter_profile',
                'linkedin_profile', 'instagram_profile', 'youtube_profile'
            )
        }),
        ('Contact', {
            'fields': ('email', 'phone_number')
        }),
        ('Interests', {
            'fields': ('interests_or_hobbies', 'subscribed_categories')
        }),
    )
