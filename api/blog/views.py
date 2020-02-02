from rest_framework import viewsets
from .models import BlogComments, Posts
from .serializers import BlogCommentsSerializer, PostsSerializer

# Create your views here.


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('-date')
    serializer_class = PostsSerializer
    filterset_fields = ['title']


class BlogCommentsViewSet(viewsets.ModelViewSet):
    queryset = BlogComments.objects.all().order_by('-date')
    serializer_class = BlogCommentsSerializer
