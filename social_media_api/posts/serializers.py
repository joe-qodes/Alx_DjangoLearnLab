from rest_framework import serializers
from .models import Post, Comment, Like
from accounts.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author", "created_at", "updated_at"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ["author", "created_at", "updated_at"]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']
        read_only_fields = ['user', 'created_at']
