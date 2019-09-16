from rest_framework.generics import ListAPIView, RetrieveAPIView
from posts.models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    # lookup_field = 'slug'  # get the "slug" instead of "pk or id" in a detail view, to do this change the <int:pk>
    # to <slug:slug> in the urls.py



