from django.db import models
from django.db import models
from django.core.validators import MinValueValidator
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.cache import cache


class Post(models.Model):
    tanks = 'TK'
    healers = 'HL'
    damage_dealers = 'DD'
    merchants = 'MR'
    guild_masters = 'GM'
    quest_givers = 'QG'
    smiths = 'SM'
    leather_workers = 'LW'
    potion_masters = 'PM'
    enchanters = 'EH'

    TYPE = [
        (tanks, 'Танки'),
        (healers, 'Хилеры'),
        (damage_dealers, 'ДД'),
        (merchants, 'Торговцы'),
        (guild_masters, 'Гильдмастера'),
        (quest_givers, 'Квестгиверы'),
        (smiths, 'Кузнецы'),
        (leather_workers, 'Кожевники'),
        (potion_masters, 'Зельевары'),
        (enchanters, 'Мастера заклинаний')
    ]
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=8, choices=TYPE, default='tank')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}') # затем удаляем его из кэша, чтобы сбросить его


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Author(models.Model):
    name = models.CharField(
        default='NoName',
        max_length=64,
        verbose_name='name of author'
    )


class UserResponse(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(default=False)