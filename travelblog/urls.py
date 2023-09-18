"""
URL patterns for a Django blog application.
It includes patterns for listing posts, viewing post details,
creating, editing, and deleting posts,
managing categories, liking/disliking posts, and adding comments.
"""
from django.urls import path
from .views import (
    PostList,
    PostDetailView,
    CreatePostView,
    EditPostView,
    DeletePostView,
    AddCategoryView,
    CategoryView,
    CategoryListView,
    EditCategoryView,
    DeleteCategoryView,
    LikeDislikePost,
    AddCommentView,
)


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('category_list/', CategoryListView, name='category_list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path(
        'templates/create_post/',
        CreatePostView.as_view(),
        name='create_post'
    ),
    path(
        'templates/add_category/',
        AddCategoryView.as_view(),
        name='add_category'
    ),
    path(
        'templates/edit_post/<slug:slug>/',
        EditPostView.as_view(),
        name='edit_post'
    ),
    path(
        'templates/<slug:slug>/remove',
        DeletePostView.as_view(),
        name='delete_post'
    ),
    path(
        'category/<slug:cats>/',
        CategoryView,
        name='category'
    ),
    path(
        'templates/edit_category/<slug:slug>/',
        EditCategoryView.as_view(),
        name='edit_category'
    ),
    path(
        'templates/delete_category/<slug:slug>/',
        DeleteCategoryView.as_view(),
        name='delete_category'
    ),
    path('like_dislike/<int:pk>/', LikeDislikePost, name='like_dislike_post'),
    path(
        'templates/<int:pk>/comment/',
        AddCommentView.as_view(),
        name='add_comment'
    ),
]
