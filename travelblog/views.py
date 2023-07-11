from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm


class PostList(ListView):
    """A class-based view that displays a list of published posts.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 6


class PostDetailView(DetailView):
    """
    View for displaying the detail of a blog post.
    This view renders the detailed information of a specific blog post,
    including its title, content, author, and other relevant details.
    """
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(CreateView):
    """
    View for creating a new blog post.
    This view provides a form to create a new blog post.
    The form includes fields such as title, title tag, author,
    categories, body content, featured image, excerpt, and status.
    """
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
