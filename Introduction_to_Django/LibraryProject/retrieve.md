
---
# `retrieve.md`

```markdown
# Retrieve Book Instance

## Django Shell Command

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
