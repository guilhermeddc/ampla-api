from django.db import models
import os

# Create your models here.


def photos_upload_path(instance, filename):
    base_name = os.path.basename(filename)
    path = f'static/{instance.name}/{base_name}'
    return path


class Provider(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Forndecedor'
        verbose_name_plural = 'Forndecedores'

    def __str__(self):
        return self.name

class Category(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Product(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    name = models.CharField('Nome do produto', max_length=100)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    description = models.TextField('Descrição')
    sold = models.BooleanField('Vendido', default=False)
    photo01 = models.ImageField(
        'Foto 01', upload_to=photos_upload_path, null=False)
    photo02 = models.ImageField(
        'Foto 02', upload_to=photos_upload_path, null=True)
    photo03 = models.ImageField(
        'Foto 03', upload_to=photos_upload_path, null=True)
    photo04 = models.ImageField(
        'Foto 04', upload_to=photos_upload_path, null=True)
    category = models.ForeignKey(
        Category, verbose_name='Categoria', on_delete=models.CASCADE)
    provider = models.ForeignKey(
        Provider, verbose_name='Fornecedor', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name


class ProductComments(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    name = models.CharField('Nome', max_length=100)
    body = models.TextField('Comentário')
    date = models.DateTimeField('Criado em ', auto_now_add=True)
    accepted = models.BooleanField('Aprovado', default=False)
    product_id = models.ForeignKey(
        Product, verbose_name='Produto relacionado', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comentário de Produto'
        verbose_name_plural = 'Comentários de Produto'
        ordering = ['date']

    def __str__(self):
        return self.name
