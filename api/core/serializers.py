from rest_framework.serializers import ModelSerializer
from .models import Category, Product, ProductComments, Provider


class ProductCommentsSerializer(ModelSerializer):
    class Meta:
        model = ProductComments
        fields = ['id', 'name', 'body', 'date', 'product_id' ]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):
    category = CategorySerializer()
    provider = ProviderSerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'sold', 'category',
                  'provider', 'photo01', 'photo02', 'photo03', 'photo04')
