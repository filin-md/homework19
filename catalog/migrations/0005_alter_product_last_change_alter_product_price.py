# Generated by Django 4.2.4 on 2023-08-21 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_category_created_at_alter_product_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_change',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена за покупку'),
        ),
    ]
