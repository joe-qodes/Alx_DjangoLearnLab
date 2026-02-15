













# Blog Post Management Features

## Overview
This Django project allows users to create, read, update, and delete blog posts (CRUD).

## Features
- **ListView**: Shows all posts.
- **DetailView**: Shows post details.
- **CreateView**: Authenticated users can create posts.
- **UpdateView**: Only post authors can edit posts.
- **DeleteView**: Only post authors can delete posts.

## Permissions
- All users can view posts.
- Only logged-in users can create posts.
- Only authors can edit or delete their own posts.

## URLs
- `/posts/` → List all posts
- `/posts/new/` → Create a new post
- `/posts/<pk>/` → View post detail
- `/posts/<pk>/edit/` → Edit post
- `/posts/<pk>/delete/` → Delete post
