from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents a book author.

    This model stores basic information about an author.
    One Author can have many Books (one-to-many relationship).
    """
    name = models.TextField()

    def __str__(self):
        return f'Author name: {self.name}' 
    


class Book(models.Model):
    """
    Represents a book written by an Author.

    Each Book is linked to exactly one Author using a ForeignKey.
    The related_name 'books' allows us to access all books of an author
    using: author.books.all()
    """
    title = models.TextField()
    publication_year = models.IntegerField(max_length=4)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name = 'books'
        )
    
    def __str__(self):
        return f'Title: {self.title}'
