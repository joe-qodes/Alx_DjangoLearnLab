from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date"]

class ExampleForm(forms.Form):
    """
    Example form used to demonstrate secure form handling
    and CSRF protection.
    """
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)