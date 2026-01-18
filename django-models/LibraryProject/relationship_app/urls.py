from django.urls import path
from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register,
    UserLoginView,
    user_logout,
)


urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]