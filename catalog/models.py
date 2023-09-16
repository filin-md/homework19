from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import User

# Create your models here.


NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')


    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name= 'Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена за покупку')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    last_change = models.DateTimeField(default=timezone.now, verbose_name='Дата последнего изменения')

    creator = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='пользователь')


    def __str__(self):
        return f'{self.product_name} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('price',)


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт',)
    version_number = models.PositiveSmallIntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    version_sign = models.TextField(verbose_name='признаки версии')

    def __str__(self):
        return f'{self.version_number} - {self.version_name}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'версии'







