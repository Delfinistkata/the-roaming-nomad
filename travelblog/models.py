"""
This module contains Django model imports for this blog application.
These imports are defining the blog's data models,
handling user authentication,
generating URLs, managing image uploads with Cloudinary,
and incorporating rich text content editing with CKEditor.
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

STATUS = ((0, "Draft"), (1, "Published"))

# Model for Category


class Category(models.Model):
    """
    This model represents categories that can be assigned
    to blog posts to organize them.
    It includes a field for the category name
    and provides a human-readable plural name.
    The '__str__' method returns a string representation of the category name,
    and 'get_absolute_url' generates the URL for viewing
    all posts in the category.
    """
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True)

    class Meta:
        """
        Options for the Category model.
        """
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        """ Returns a string representation of the category_name. """
        return str(self.category_name)

    def get_absolute_url(self):
        """ Returns the absolute URL for the category. """
        return reverse('category', args=[str(self.category_name)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    """
    Model representing user profiles with additional information.
    This model extends the default User model with
    additional fields to store user profile information.
    It includes fields for personal details,
    social media profiles, contact information, and more.
    The '__str__' method returns the username of the associated user,
    and 'get_absolute_url' generates the URL for
    viewing the user's profile page.
    """
    user = models.OneToOneField(User, null=True,  on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = CloudinaryField('image', default='placeholder')
    date_of_birth = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook_profile = models.CharField(max_length=255, blank=True, null=True)
    twitter_profile = models.CharField(max_length=255, blank=True, null=True)
    linkedin_profile = models.CharField(max_length=255, blank=True, null=True)
    instagram_profile = models.CharField(max_length=255, blank=True, null=True)
    youtube_profile = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=100, blank=True)
    interests_or_hobbies = models.TextField(blank=True)
    subscribed_categories = models.ManyToManyField(Category, blank=True)

    def __str__(self) -> str:
        """ Returns a string representation of the associated user. """
        return str(self.user)

    def get_absolute_url(self):
        """ Returns the absolute URL for the user's profile page. """
        return reverse('show_user_profile_page', args=[str(self.pk)])

    def is_complete(self):
        """
        Checks if the user's profile is considered complete.
        """
        required_fields = [
            'bio',
        ]

        for field_name in required_fields:
            if not getattr(self, field_name):
                return False

        return True


class Post(models.Model):
    """ Model representing a blog post. """
    title = models.CharField(max_length=200, unique=True)
    title_tag = models.CharField(max_length=200, default="The Roaming Nomad")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    categories = models.ManyToManyField(Category)
    body_content = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    post_number = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)
    dislikes = models.ManyToManyField(
        User, related_name='blog_dislikes', blank=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)
    excerpt = models.CharField(max_length=255)

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
        """
        Overrides the save method to automatically
        generate the post's slug.
        """
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
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments'
    )
    date_posted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        '''
        The `ordering` attribute specifies the default ordering
        of Comment instances by the `date_posted` field in descending order.
        '''
        ordering = ['date_posted']

    def __str__(self):
        author = (
            f"{self.author.first_name} {self.author.last_name}"
            if self.author.first_name
            else self.author.username
        )
        return f"Comment by {author} on {self.post}"
