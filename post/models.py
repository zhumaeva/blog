from django.db import models
from django.db.models import query
from django.db.models.base import Model
from django.db.models.fields import CharField, SlugField
from django.db.models.fields.related import ForeignKey
from django.conf import settings
from django.urls import reverse

class Tag(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='слаг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def get_absolute_url(self):
        return reverse('posts_by_tag', kwargs={'slug': self.slug})


class Category(models.Model):

    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(verbose_name='Слаг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts_by_category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Post(models.Model):

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликован')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор', 
                                related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', 
                                related_name='posts')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    slug = models.SlugField(verbose_name='Слаг')
    views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    photo = models.ImageField(upload_to='posts/%Y/%m/%d/',verbose_name = 'Фото', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})