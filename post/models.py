import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# SQL -> 
"""
    CREATE TABLE Post(
        id SERIAL PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        text TEXT NULL,
        image VARCHAR(20) NULL
    )
"""

# ORM -> 
class Post(models.Model):
    #id = models.UUIDField()
    name = models.CharField('Название',max_length=20, null=True, blank=True)
    text = models.TextField('Контент', null=True, blank=True)
    image = models.ImageField('Изображение',upload_to='post/%Y/%m/%d', null=True, blank=True)
    price = models.DecimalField('Цена',max_digits=3, decimal_places=2, null=True, blank=True) #999.32 -> 
    like = models.BooleanField('Нравится',default=False, null=True, blank=True)
    date = models.DateField('Дата', blank=True, null=True, auto_now_add=True)
    slug = models.SlugField('Слаг',max_length=100, blank=True, null=True)
    author = models.ForeignKey(to=User, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Автор')
    categories = models.ManyToManyField(to='Category')

    def get_absolute_url(self):
        return reverse("about_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

class Category(models.Model):
    name = models.CharField('Название', max_length=30, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Comment(models.Model):
    post = models.OneToOneField(to=Post, on_delete=models.CASCADE, verbose_name='Пост')
    user = models.CharField('Имя', max_length=20)
    text = models.TextField('Текст')
    date = models.DateField('Название', auto_now_add=True)
    active = models.BooleanField('Активность', default=False)

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарии'

    def __str__(self) -> str:
        return self.user
