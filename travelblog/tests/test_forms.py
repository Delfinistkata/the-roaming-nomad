"""
Module containing test cases for various
forms used in the travelblog application.
"""
from django.test import TestCase
from travelblog.forms import PostForm, EditForm, CategoryEditForm, CommentForm


class PostFormTest(TestCase):
    """
    Tests cases for the PostForm.
    """
    def test_valid_post_form(self):
        """
        Tests the validity of the PostForm with valid data.
        """
        data = {
            'title': 'Test Title',
            'title_tag': 'Test Tag',
            'categories': [1, 2],
            'body_content': 'Test content',
            'featured_image': 'test.jpg',
            'excerpt': 'Test excerpt',
            'status': 1,
        }
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

        form = PostForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_post_form(self):
        """
        Tests the validity of the PostForm with missing or invalid data.
        """
        data = {}
        form = PostForm(data=data)
        self.assertFalse(form.is_valid())


class EditFormTest(TestCase):
    """
    Tests cases for the EditForm.
    """
    def test_valid_edit_form(self):
        """
        Tests the validity of the EditForm with valid data.
        """
        data = {
            'title': 'Updated Title',
            'title_tag': 'Updated Tag',
            'categories': [1],
            'body_content': 'Updated content',
            'featured_image': 'updated.jpg',
            'excerpt': 'Updated excerpt',
            'status': 1,
        }
        form = EditForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_edit_form(self):
        """
        Test the validity of the EditForm with missing or invalid data.
        """
        data = {}
        form = EditForm(data=data)
        self.assertFalse(form.is_valid())


class CategoryEditFormTest(TestCase):
    """
    Tests cases for the CategoryEditForm.
    """
    def test_valid_category_edit_form(self):
        """
        Test the validity of the CategoryEditForm with valid data.
        """
        data = {
            'category_name': 'Updated Category Name',
        }
        form = CategoryEditForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_category_edit_form(self):
        """
        Test the validity of the CategoryEditForm with missing or invalid data.
        """
        data = {}
        form = CategoryEditForm(data=data)
        self.assertFalse(form.is_valid())


class CommentFormTest(TestCase):
    """
    Tests cases for the CommentForm.
    """
    def test_valid_comment_form(self):
        """
        Tests the validity of the CommentForm with valid data.
        """
        data = {
            'author': 'John Doe',
            'body_content': 'Test comment content',
        }
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_comment_form(self):
        """
        Test the validity of the CommentForm with missing or invalid data.
        """
        data = {}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
