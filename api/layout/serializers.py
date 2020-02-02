from rest_framework import serializers
from .models import IntroProject, IntroSlide, Testimonials


class IntroProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntroProject
        fields = ['id', 'title', 'subtitle', 'description',
                  'photo01', 'photo02', 'photo03', 'photo04']


class IntroSlideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntroSlide
        fields = ['id', 'title', 'imageBackground', 'logo',
                  'link', 'route']


class TestimonialsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Testimonials
        fields = ['id', 'image', 'client', 'architect',
                  'description']
