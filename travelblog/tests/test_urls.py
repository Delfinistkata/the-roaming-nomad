"""
This module contains test cases for the travelblog app.
It tests various aspects of the app, including URL patterns,
model behaviors, and view functionalities.
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from travelblog.models import Post, Category


class UrlsTestCase(TestCase):
    """
    Test case for testing URL patterns.
    """
    def test_home_url_returns_200_ok(self):
        """
        Test the 'home' URL pattern.
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_list_url_returns_200_ok(self):
        """
        Test the 'category_list' URL pattern.
        """
        url = reverse('category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_returns_200_ok(self):
        """
        Test the 'post_detail' URL pattern with a slug parameter.
        """
        post = Post.objects.create(
            title='Test Post',
            author=User.objects.create_user(
                username='testuser',
                password='testpassword',
                ),
            body_content='This is a test post content.',
            slug='test-post',
        )
        url = reverse('post_detail', kwargs={'slug': post.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_like_dislike_post_url_returns_200_ok(self):
        """
        Test the 'like_dislike_post' URL pattern with an int parameter.
        """
        post = Post.objects.create(
            title='Test Post',
            author=User.objects.create_user(
                username='testuser',
                password='testpassword'
            ),
            body_content='This is a test post content.',
            slug='test-post',
        )
        url = reverse('like_dislike_post', kwargs={'pk': post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_comment_url_returns_200_ok(self):
        """
        Test the 'add_comment' URL pattern with an int parameter.
        """
        post = Post.objects.create(
            title='Test Post',
            author=User.objects.create_user(
                username='testuser',
                password='testpassword'
            ),
            body_content='This is a test post content.',
            slug='test-post',
        )
        url = reverse('add_comment', kwargs={'pk': post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class PostModelTestCase(TestCase):
    """
    Test case for testing the Post model.
    """
    def setUp(self):
        """
        Set up test data.
        """
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        # Create a test category
        self.category = Category.objects.create(
            category_name='Test Category'
        )

    def test_create_post(self):
        """
        Test creating a post.
        """
        post = Post.objects.create(
            title='Test Post',
            author=self.user,
            body_content='This is a test post.',
            slug='test-post',
        )
        self.assertEqual(str(post), 'Test Post')
        self.assertEqual(post.number_of_likes(), 0)
        self.assertEqual(post.number_of_dislikes(), 0)
        self.assertEqual(post.get_absolute_url(), '/test-post/')

    def test_slug_generation(self):
        """
        Test slug generation for a post.
        """
        post = Post.objects.create(
            title='Another Test Post',
            author=self.user,
            body_content='This is another test post.',
        )
        self.assertEqual(post.slug, 'another-test-post')

    def test_like_dislike_count(self):
        """
        Test counting likes and dislikes for a post.
        """
        post = Post.objects.create(
            title='Count Test Post',
            author=self.user,
            body_content=(
                'This is a test post for counting likes '
                'and dislikes.',
            )
        )
        # Simulates user likes and dislikes
        user1 = User.objects.create_user(
            username='user1',
            password='user1pass'
        )
        user2 = User.objects.create_user(
            username='user2',
            password='user2pass'
        )
        post.likes.add(user1)
        post.dislikes.add(user2)

        self.assertEqual(post.number_of_likes(), 1)
        self.assertEqual(post.number_of_dislikes(), 1)
