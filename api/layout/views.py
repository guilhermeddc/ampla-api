from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import IntroProject, IntroSlide, Testimonials
from .serializers import IntroProjectSerializer, IntroSlideSerializer, TestimonialsSerializer

# Create your views here.


class IntroProjectViewSet(viewsets.ModelViewSet):
    queryset = IntroProject.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = IntroProjectSerializer


class IntroSlideViewSet(viewsets.ModelViewSet):
    queryset = IntroSlide.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = IntroSlideSerializer


class TestimonialsViewSet(viewsets.ModelViewSet):
    queryset = Testimonials.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TestimonialsSerializer
