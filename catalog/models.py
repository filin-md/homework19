from django.db import models
from django.utils import timezone

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
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена за покупку')
    create_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    last_change = models.DateTimeField(default=timezone.now, verbose_name='Дата последнего изменения')


    def __str__(self):
        return f'{self.product_name} {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('price',)


