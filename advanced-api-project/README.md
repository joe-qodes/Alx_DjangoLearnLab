# Advanced API Project - Views Documentation

This section explains how the Book API views are configured, their behavior, and any custom hooks or settings.

## Views Overview

| View | URL | Purpose | Permissions | Notes / Hooks |
|------|-----|---------|------------|---------------|
| BookListView | /api/books/ | List all books | Public (AllowAny) | Uses `ListAPIView`; no custom hooks |
| BookDetailView | /api/books/<id>/ | Retrieve a single book by ID | Public (AllowAny) | Uses `RetrieveAPIView`; DRF handles object retrieval via pk |
| BookCreateView | /api/books/create/ | Add a new book | Authenticated only | Uses `CreateAPIView`; validates `publication_year` via serializer |
| BookUpdateView | /api/books/<id>/update/ | Modify an existing book | Authenticated only | Uses `UpdateAPIView`; supports full or partial updates; validation handled by serializer |
| BookDeleteView | /api/books/<id>/delete/ | Remove a book | Authenticated only | Uses `DestroyAPIView`; deletion handled automatically |

## Custom Settings and Hooks

- **Validation Hooks**: `BookSerializer` validates that `publication_year` is not in the future.
- **Permissions**: Controlled per view via `permission_classes`.
- **Generic Behavior**: All views rely on DRF generics to handle CRUD operations. No custom methods (`get()`, `post()`, etc.) are implemented.
- **Nested Serialization**: Related Author data is included when using BookSerializer in nested contexts, but the views themselves remain flat.
- **Error Handling**: DRF automatically returns 400/403/404 responses for validation, authentication, and object lookup errors.

## Testing

- Use Postman, curl, or Django shell to test each endpoint.
- Ensure proper authentication for create, update, and delete endpoints.
- Public endpoints can be accessed without login.


# Filtering, Searching, and Ordering in the Book API

This project enhances the Book API by adding advanced query capabilities using Django REST Framework’s built-in filtering tools. These features allow API users to retrieve data efficiently by narrowing results based on specific criteria.

The following functionalities were added to the `BookListView`:

- Filtering by model fields
- Searching using text queries
- Ordering results by selected fields

These capabilities are implemented using:

- `DjangoFilterBackend`
- `SearchFilter`
- `OrderingFilter`

---

## Implementation in `views.py`

The `BookListView` was updated to include multiple filter backends:

```python
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

-

"""
Inside the view:

class BookListView(generics.ListAPIView):
    """
    List all books with advanced query capabilities:
    - Filtering by title, author, publication_year
    - Searching by title and author
    - Ordering by title and publication_year
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

Configuration in settings.py

To enable filtering globally, the following configuration was added:

INSTALLED_APPS = [
    ...
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ]
}

How to Use These Features in API Requests

All features work through query parameters on the /books/ endpoint.

Base endpoint:

/books/

1. Filtering

Filter books by exact field values.

Examples:

/books/?title=Things Fall Apart
/books/?publication_year=1958
/books/?author=1

2. Searching

Perform partial text search on title or author.

Examples:

/books/?search=achebe
/books/?search=things

3. Ordering

Sort results by specific fields.

Examples:

/books/?ordering=title
/books/?ordering=-publication_year


- indicates descending order.

4. Combining Features

These features can be used together in a single request.

Example:

/books/?search=achebe&ordering=-publication_year

"""
