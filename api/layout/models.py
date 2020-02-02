from django.db import models
from core.models import Product
from blog.models import Posts
import os

# Create your models here.


def photos_upload_path(instance, filename):
    base_name = os.path.basename(filename)
    path = f'static/{instance.slug}/{base_name}'
    return path


class IntroSlide(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    imageBackground = models.ImageField(
        'Foto de fundo', upload_to=photos_upload_path, null=False)
    logo = models.ImageField(
        'Logo', upload_to=photos_upload_path, null=True)
    title = models.CharField('Título', max_length=100, null=True, blank=True, default='')
    ROUTE_CHOICES = [( 'blog', 'Blog'), ( 'produto', 'Produtos'), ( 'produtos', 'Loja')]
    route = models.CharField('Rota', max_length=10, choices=ROUTE_CHOICES, null=True, blank=True, default='Sem Rota')
    link = models.BooleanField('Link', default=False)
    product = models.ForeignKey(
        Product, verbose_name='Produto', on_delete=models.DO_NOTHING, null=True, blank=True)
    posts = models.ForeignKey(
        Posts, verbose_name='Post', on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        verbose_name = 'Slide da introdução'
        verbose_name_plural = 'Slides da introdução'

    def __str__(self):
        return self.title


class IntroProject(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    title = models.CharField('Título', max_length=100, null=False)
    subtitle = models.CharField('SubTítulo', max_length=100, null=False)
    description = models.TextField('Descrição', null=False)
    photo01 = models.ImageField(
        'Foto 01', upload_to=photos_upload_path, null=False)
    photo02 = models.ImageField(
        'Foto 02', upload_to=photos_upload_path, null=False)
    photo03 = models.ImageField(
        'Foto 03', upload_to=photos_upload_path, null=False)
    photo04 = models.ImageField(
        'Foto 04', upload_to=photos_upload_path, null=False)
    date = models.DateTimeField('Criado em ', auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Slide do Projeto'
        verbose_name_plural = 'Slides dos Projetos'

    def __str__(self):
        return self.title


class Testimonials(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    image = models.ImageField(
        'Imagem', upload_to=photos_upload_path, null=False)
    client = models.CharField('Cliente', max_length=100, null=False)
    architect = models.CharField('Arquiteto', max_length=100, null=False)
    description = models.TextField('Descrição', null=False)
    date = models.DateTimeField('Criado em ', auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.architect
