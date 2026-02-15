# blog/urls.py

from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView
)

urlpatterns = [
    # Posts
    path('post/', PostListView.as_view(), name='post-list'),            # List all posts
    path('post/new/', PostCreateView.as_view(), name='post-create'),    # Create new post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # View single post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comments
    path('post/<int:pk>/comments/new/', CommentCreateView, name='comment-add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

    # Authentication & profile
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("", views.home_view, name="home"),

    path('search/', views.search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]
