
---

# `delete.md`

```markdown
# Delete Book Instance

## Django Shell Command

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
