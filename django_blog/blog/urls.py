from django.urls import path
from . import views
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, add_comment, CommentUpdateView, CommentDeleteView
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name= "logout"),
    path("profile/", views.profile_view, name="profile"),
    path("", views.home_view, name="home"),
    path("post/", views.posts_view, name="posts"),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post-list'), name='logout'),
    # Comments
    path('post/<int:post_id>/comments/new/', views.CommentCreateView, name='comment-add'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]