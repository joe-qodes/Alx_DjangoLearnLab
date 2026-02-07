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


