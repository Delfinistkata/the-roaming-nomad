from django.urls import path
from .views import PostList, PostDetailView, CreatePostView, EditPostView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('templates/create_post/', CreatePostView.as_view(), name='create_post'),
    path('templates/edit_post/<slug:slug>/', EditPostView.as_view(), name='edit_post'),
]
