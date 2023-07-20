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
from .models import Post, Category, Comment


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
                    'approved', 'number_of_comment_likes',
                    'number_of_comment_dislikes')
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

    def number_of_comment_likes(self):
        '''
        It calculates and returns the total number of likes
        that the comment has received.
        '''
        # pylint: disable=E1101
        return str(self.comment_likes.count())

    def number_of_comment_dislikes(self):
        '''
        It calculates and returns the total number of dislikes
        that the comment has received.
        '''
        # pylint: disable=E1101
        return str(self.comment_dislikes.count())


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'post_count',)

    def post_count(self, obj):
        """
        Method to display the count of associated posts
        for each category.
        """
        return obj.post_set.count()

    post_count.short_description = 'Post Count'
