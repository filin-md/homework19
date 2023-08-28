from django.db import models
from django.utils import timezone

# Create your models here.


NULLABLE = {'null': True, 'blank': True}

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Загловок')
    slug = models.CharField(max_length=100, verbose_name='ЧПУ', **NULLABLE)
    content = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    published = models.BooleanField(default=True, verbose_name='Статус публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return {self.title}\

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

