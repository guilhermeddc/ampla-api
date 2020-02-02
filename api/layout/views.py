from rest_framework import viewsets
from .models import IntroProject, IntroSlide, Testimonials
from .serializers import IntroProjectSerializer, IntroSlideSerializer, TestimonialsSerializer

# Create your views here.


class IntroProjectViewSet(viewsets.ModelViewSet):
    queryset = IntroProject.objects.all()
    serializer_class = IntroProjectSerializer


class IntroSlideViewSet(viewsets.ModelViewSet):
    queryset = IntroSlide.objects.all()
    serializer_class = IntroSlideSerializer


class TestimonialsViewSet(viewsets.ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
