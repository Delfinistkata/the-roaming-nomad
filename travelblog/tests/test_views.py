"""
This module contains test cases for the views of this application.
It tests the functionality of various views, such as listing posts,
viewing post details, creating, editing, and deleting posts,
and ensures that these views behave as expected.
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from travelblog.models import Post, Category


class TestPostViews(TestCase):
    """
    Test cases for the views of the application.
    """
    def setUp(self):
        """
        Set up test data.
        """
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a test category
        self.category = Category.objects.create(
            category_name='Test Category'
        )

        # Create a test post
        self.test_post = Post.objects.create(
            title='Test Post',
            body_content='This is a test post content.',
            author=self.user,
            status=1,  # 1 for Published
            excerpt='Test excerpt',
        )

    def test_post_list_view(self):
        """
        Test the post list view.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        """
        Test the post detail view.
        """
        response = self.client.get(
            reverse('post_detail', kwargs={'slug': self.test_post.slug})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_create_post_view(self):
        """
        Test the create post view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('create_post'), {
            'title': 'New Post',
            'body_content': 'This is a new post.',
            'author': self.user.id,
            'categories': [self.category.id],
            'status': 1,
            'excerpt': 'New excerpt',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)

    def test_edit_post_view(self):
        """
        Test the edit post view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('edit_post', kwargs={'slug': self.test_post.slug}),
            {
                'title': 'Updated Test Post',
                'body_content': 'This is an updated post content.',
                'status': 1,
                'excerpt': 'Updated excerpt',
            }
        )
        self.test_post.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.test_post.title, 'Updated Test Post')

    def test_delete_post_view(self):
        """
        Test the delete post view.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('delete_post', kwargs={'slug': self.test_post.slug})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 0)
