from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from .models import BlogComments, Posts
from .serializers import BlogCommentsSerializer, PostsSerializer

# Create your views here.


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('-date')
    serializer_class = PostsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    filterset_fields = ['title']


class BlogCommentsViewSet(viewsets.ModelViewSet):
    queryset = BlogComments.objects.all().order_by('-date')
    serializer_class = BlogCommentsSerializer
    filterset_fields = ['title']
