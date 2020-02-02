from rest_framework.serializers import ModelSerializer
from .models import Posts, BlogComments


class PostsSerializer(ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'slug', 'title', 'description',
                  'content', 'author', 'date', 'image']


class BlogCommentsSerializer(ModelSerializer):
    class Meta:
        model = BlogComments
        fields = ['id', 'name', 'body', 'date', 'posts']
