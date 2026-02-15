from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.models import User

from .models import Post

def posts_view(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, "blog/posts.html", {"posts": posts})

#register view
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form})

# profile management view
@login_required
def profile_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = request.user
        user.email = email
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("profile")
    return render(request, "blog/profile.html", {"user": request.user})

# login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect("home")  # redirect to homepage view
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "blog/login.html")

#logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")

# Profile management view
@login_required
def profile_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = request.user
        user.email = email
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect("profile")
    return render(request, "blog/profile.html", {"user": request.user})

def home_view(request):
    return render(request, "blog/home.html")
