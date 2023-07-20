from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify
from .models import Post, Category
from .forms import PostForm, EditForm, CategoryEditForm


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


def CategoryListView(request):
    """
    View to display a list of all categories.
    This view retrieves all categories from the database and passes them to the
    'category_list.html' template, where they are displayed as a list.
    """
    category_list_menu = Category.objects.all()
    return render(
        request,
        'category_list.html',
        {'category_list_menu': category_list_menu}
    )


def CategoryView(request, cats):
    """
    View to display a specific category and its associated posts.
    This view retrieves the category specified
    by the 'cats' parameter from the database.
    It then queries the posts associated with that category
    and passes them along with
    the category object to the 'category.html' template for rendering.
    """
    category_name = cats.replace('-', ' ').title()
    category = Category.objects.get(category_name__iexact=category_name)
    category_posts = Post.objects.filter(categories=category)
    return render(
        request,
        'category.html',
        {'category': category, 'category_posts': category_posts}
    )


class AddCategoryView(CreateView):
    """
    View to add a new category.
    This view uses Django's CreateView to handle
    the creation of a new category object.
    The view uses the 'add_category.html' template for rendering the form.
    """
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


class EditCategoryView(UpdateView):
    """
    View for editing a specific category.
    """
    model = Category
    form_class = CategoryEditForm
    template_name = 'edit_category.html'
    slug_url_kwarg = 'category_name'
    slug_field = 'category_name'
    success_url = reverse_lazy('category_list')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        category_name = slugify(slug)
        return get_object_or_404(Category, category_name__iexact=category_name)


class DeleteCategoryView(DeleteView):
    """
    View to delete a category.

    This view uses Django's DeleteView to handle
    the deletion of a category object.
    The view retrieves the category to delete using the 'slug' URL parameter
    and slugifies it to match the 'category_name' field.
    The view uses the 'delete_category.html'
    template for rendering the confirmation page.
    """
    model = Category
    template_name = 'delete_category.html'
    slug_url_kwarg = 'category_name'
    slug_field = 'category_name'
    success_url = reverse_lazy('category_list')

    def get_object(self, queryset=None):
        """
        Get the category object to delete based on the slug URL parameter.
        """
        slug = self.kwargs.get('slug')
        category_name = slugify(slug)
        return get_object_or_404(Category, category_name__iexact=category_name)
