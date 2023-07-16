from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Post, Category
from .forms import PostForm, EditForm


class PostList(ListView):
    """A class-based view that displays a list of published posts.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = 'index.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset().filter(status=1)

        category_filter = self.request.GET.getlist('category')
        if category_filter:
            queryset = queryset.filter(categories__id__in=category_filter)

        return queryset.order_by("-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    """
    View for displaying the detail of a blog post.
    This view renders the detailed information of a specific blog post,
    including its title, content, author, and other relevant details.
    """
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


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

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.post_number = Post.objects.count()
        self.object.save()
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context


class EditPostView(UpdateView):
    """
    View for editing a specific post.
    Inherits from Django's UpdateView class.
    """
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'


class DeletePostView(DeleteView):
    """
    View for deleting a specific post.
    Inherits from Django's DeleteView class.
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
