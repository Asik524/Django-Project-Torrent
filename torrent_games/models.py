from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Games(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название игр')
    context = models.TextField(verbose_name='Описание игры')
    system_requirements = models.TextField(verbose_name='Системные требования:')
    photo = models.ImageField(upload_to='photo/', verbose_name='Фото')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    changes = models.CharField(max_length=100, null=True, blank=True, verbose_name='Изменение')
    release_date_game = models.CharField(max_length=100, null=True, verbose_name='Дата выхода')
    genre_game = models.CharField(max_length=100, null=True, verbose_name='Жанр')
    developer = models.CharField(max_length=100, null=True, verbose_name='Разработчик')
    publisher = models.CharField(max_length=100, null=True, verbose_name='Издательство')
    platform = models.CharField(max_length=100, null=True, verbose_name='Платформа')
    repack = models.CharField(max_length=100, null=True, verbose_name='Тип издания')
    interface_language = models.CharField(max_length=100, null=True, verbose_name='Язык интерфейса')
    voice_over_language = models.CharField(max_length=100, null=True, verbose_name='Язык озвучки')
    tablet = models.CharField(max_length=100, null=True, verbose_name='Таблeтка')
    video = models.CharField(max_length=255, verbose_name='Ссылка видео', null=True)
    uploads = models.IntegerField(default=0, null=True, verbose_name='Скачали: ')
    repack_and_repack_size = models.CharField(max_length=100, null=True, verbose_name='Размер игры или Репак и размер репака')
    download = models.FileField(upload_to='Downloads/', null=True, blank=True, verbose_name='Файл для скачивания')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Игру'
        verbose_name_plural = 'Игры'



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name='Фото профиля')
    phone_number = models.CharField(max_length=30, blank=True, null=True, verbose_name='Номер телефона')
    about_user = models.CharField(max_length=100, blank=True, null=True, verbose_name='О себе')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Адрес')

    def __str__(self):
        return self.user.username

    def get_photo_user(self):
        try:
            return self.photo.url
        except:
            return 'https://sun9-79.userapi.com/impg/Om5Z4CI8nPt8d7Z3H2aYRoXcp4SQ4OXxYF2q7A/vb8McJOD5jg.jpg?size=750x750&quality=95&sign=66a5016f42cedbfad26304339930d204&c_uniq_tag=oUh1Y6hOnXmS3rOdJneqHru14rgqvQmD4aME8nXhA7k&type=album'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Коментатор')
    game = models.ForeignKey(Games, on_delete=models.CASCADE, verbose_name='Игра')
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата коментария')

    def __str__(self):
        return self.user.username



    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
