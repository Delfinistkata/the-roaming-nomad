from django.urls import path
from .views import PostList, PostDetailView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
