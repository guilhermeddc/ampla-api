from django.core.mail import EmailMessage
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .models import Category, Product, ProductComments, Provider
from .serializers import ProductSerializer, CategorySerializer, ProductCommentsSerializer, ProviderSerializer

# Create your views here.


class ProductCommentsViewSet(viewsets.ModelViewSet):
    queryset = ProductComments.objects.all().order_by('-date')
    serializer_class = ProductCommentsSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter,]
    search_fields = ['name', 'description', 'category__name', 'provider__name']
    filterset_fields = ['category']
