from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed, like_post, unlike_post
from django.urls import path, include

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),        # keeps your posts/ and comments/ endpoints
    path('feed/', feed, name='feed'),      # new feed endpoint
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
]