"""
This module contains Django imports for various view classes,
utilities, and models
used in a blog application.
This module helps in setting up a Django blog application
by providing necessary imports
for views, forms, models, and utilities.
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy, reverse
from django.template.defaultfilters import slugify
from django.http import Http404, HttpResponse
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CategoryEditForm, CommentForm


def like_dislike_post(request, pk):
    """
    View function to handle liking and disliking a post.
    If the 'like' button is clicked and
    the user has not already liked the post,
    it adds the user to the post's likes.
    If the 'like' button is clicked and the user has already liked the post,
    it removes the user from the post's likes.
    Similarly, if the 'dislike' button is clicked,
    it adds or removes the user from the post's dislikes accordingly.
    """
    post = get_object_or_404(Post, id=pk)

    if request.method == 'POST':
        if 'like' in request.POST:
            if request.user in post.likes.all():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
                post.dislikes.remove(request.user)
        elif 'dislike' in request.POST:
            if request.user in post.dislikes.all():
                post.dislikes.remove(request.user)
            else:
                post.dislikes.add(request.user)
                post.likes.remove(request.user)
        return redirect('post_detail', slug=post.slug)
    return redirect('post_detail', slug=post.slug)


class PostList(ListView):
    """
    A class-based view that displays a list of published posts.
    This view displays a paginated list of published blog posts,
    with the option to filter by categories.
    It uses the 'model' and 'queryset' attributes to fetch
    and display the posts.
    The 'get_queryset' method further filters
    the queryset based on selected categories.
    The 'get_context_data' method adds a list of all available
    categories to the context.
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


def category_list_view(request):
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


def category_view(request, cats):
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
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        messages.success(self.request, 'Category was created successfully.')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
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
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_number = Post.objects.count() + 1
        form.instance.author = self.request.user
        messages.success(
            self.request,
            'The post has been created successfully.'
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.userprofile.is_complete():
            return redirect('create_profile_page')

        return super().dispatch(request, *args, **kwargs)


class AddCommentView(CreateView):
    """
    View for creating a new blog post.
    This view provides a form to create a new blog post.
    The form includes fields such as title, title tag, author,
    categories, body content, featured image, excerpt, and status.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPostView(UpdateView):
    """
    View for editing a specific post.
    Inherits from Django's UpdateView class.
    """
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'

    def form_valid(self, form):
        messages.success(
            self.request,
            'The post has been updated successfully.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'There was an error in updating the post.'
        )
        return super().form_invalid(form)


class DeletePostView(DeleteView):
    """
    View for deleting a specific post.
    Inherits from Django's DeleteView class.
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            'The post has been deleted successfully.'
        )
        return super().delete(request, *args, **kwargs)


class EditCategoryView(UpdateView):
    """
    View for editing a specific category.
    """
    model = Category
    form_class = CategoryEditForm
    template_name = 'edit_category.html'
    success_url = reverse_lazy('category_list')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        category_name = slugify(slug)
        return get_object_or_404(Category, slug=category_name)

    def form_valid(self, form):
        messages.success(
            self.request,
            'The category has been updated successfully.'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            'There was an error in updating the category.'
        )
        return super().form_invalid(form)


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
    success_url = reverse_lazy('category_list')

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        category_name = slugify(slug)
        return get_object_or_404(Category, slug=category_name)

    def delete(self, request, *args, **kwargs):
        messages.success(
            self.request,
            'The category has been deleted successfully.'
        )
        return super().delete(request, *args, **kwargs)


# 404 Handler
def handler_404(request, exception):
    """
    Custom error handler for handling 404 (Page Not Found) errors.
    """
    error_message = "The page you requested could not be found."
    context = {
        'error_message': error_message,
    }
    return render(request, '404_custom.html', context, status=404)


# 403 Handler
def handler_403(request, *args, **kwargs):
    """
    Custom error handler for handling 403 (Forbidden) errors.
    """
    error_message = (
        "Access not Granted. You do not have permission to access this page."
    )
    context = {'error_message': error_message}
    return render(
        request,
        '403.html',
        context,
        status=403
    )


# 500 Handler
def handler_500(request, *args, **kwargs):
    """
    Custom error handler for handling 500 (Internal Server Error) errors.
    """
    error_message = (
        "Woops! Something went wrong. We apologize for the inconvenience. "
        "Our team has been notified about this issue. "
        "Please try again later or contact support if the problem persists."
    )
    context = {'error_message': error_message}
    response = render(request, '500.html', context)
    response.status_code = 500
    return response
