from rest_framework import serializers
from .models import *
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model.

    Includes custom validation to ensure the publication year
    is not set in the future.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        """
        Ensures the publication year is not in the future.
        This runs automatically during serializer.is_valid().
        """
        if value > current_year:
            raise serializers.ValidationError("Publication year is in the future")
        return value
    

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author model and dynamically includes
    all related books using a nested BookSerializer.
    The 'books' field comes from the related_name defined
    in the Book model's ForeignKey.
    """
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    
