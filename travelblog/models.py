"""
Module containing model imports and utility functions for a blog application.
"""

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

# Model for Category


class Category(models.Model):
    """
    Model representing a category for blog posts.
    """
    category_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        """
        Returns a string representation of the category_name.
        """
        return str(self.category_name)

    def get_absolute_url(self):
        """
        Returns the absolute URL for the category.
        """
        return reverse('home')


class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200, unique=True)
    title_tag = models.CharField(max_length=200, default="The Roaming Nomad")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    categories = models.ManyToManyField(Category)
    body_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post_number = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)
    dislikes = models.ManyToManyField(
        User, related_name='blog_dislikes', blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField()

    class Meta:
        """
        This class provides meta options for the Post model.
        The `ordering` attribute specifies the default ordering
        of Post instances by the `created_on` field
        in descending order.
        """
        ordering = ['-created_on']

    def __str__(self) -> str:
        return str(self.title)

    def number_of_likes(self) -> str:
        '''
        It calculates and returns the total number of likes
        that the post has received.
        '''
        # pylint: disable=E1101
        return str(self.likes.count())

    def number_of_dislikes(self) -> str:
        '''
        It calculates and returns the total number of dislikes
        that the post has received.
        '''
        # pylint: disable=E1101
        return str(self.dislikes.count())

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Returns the absolute URL for the post.
        The absolute URL is generated based on the post's slug field
        and can be used to link to the post's detail page.
        """
        return reverse('post_detail', args=[str(self.slug)])


class Comment(models.Model):
    '''
    Model representing a comment on a blog post.
    This class represents a comment made by a user on a blog post.
    It contains information such as the associated post,
    the content of the comment, the author, the date it was posted,
    the comment number, the number of likes and dislikes,
    and whether it is approved.
    '''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="comments"
    )
    body_content = models.TextField()
    author = models.CharField(max_length=80)
    date_posted = models.DateTimeField(auto_now_add=True)
    comment_likes = models.ManyToManyField(
        User, related_name='comment_likes', blank=True)
    comment_dislikes = models.ManyToManyField(
        User, related_name='comment_dislikes', blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        '''
        The `ordering` attribute specifies the default ordering
        of Comment instances by the `date_posted` field in descending order.
        '''
        ordering = ['date_posted']

    def __str__(self):
        '''
        Returns a string representation of the comment.
        '''
        return f"Comment by {self.author} on {self.post}"

    def number_of_comment_likes(self) -> str:
        '''
        It calculates and returns the total number of likes
        that the comment has received.
        '''
        # pylint: disable=E1101
        return str(self.comment_likes.count())

    def number_of_comment_dislikes(self) -> str:
        '''
        It calculates and returns the total number of dislikes
        that the comment has received.
        '''
        # pylint: disable=E1101
        return str(self.comment_dislikes.count())
