from django.db import models
from django.dispatch import receiver
import os

# Create your models here.


def photos_upload_path(instance, filename):
    base_name = os.path.basename(filename)
    path = f'static/{instance.slug}/{base_name}'
    return path


class Posts(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    title = models.CharField('Título', max_length=254, null=False)
    description = models.TextField('Descrição', null=False)
    content = models.TextField('Conteúdo', null=False)
    author = models.CharField('Autor', max_length=100)
    date = models.DateTimeField('Criado em ', auto_now_add=True)
    image = models.ImageField(
        'Imagem', upload_to=photos_upload_path, null=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['date']

    def __str__(self):
        return self.title


class BlogComments(models.Model):
    slug = models.SlugField(max_length=50, null=True, blank=True)
    name = models.CharField('Nome', max_length=100)
    body = models.TextField('Comentário')
    date = models.DateTimeField('Criado em ', auto_now_add=True)
    accepted = models.BooleanField('Aprovado', default=False)
    posts = models.ForeignKey(
        Posts, verbose_name='Post relacionado', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Blog Comentário'
        verbose_name_plural = 'Blog Comentários'
        ordering = ['date']

    def __str__(self):
        return self.name

@receiver(models.signals.post_delete, sender=Posts.image)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=Posts.image)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).file
    except sender.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)