from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'product_name': 'ноутбук', 'description': 'мощный тонкий', 'category': Category.objects.get(pk=1), 'price': 100000},
            {'product_name': 'кресло', 'description': 'мягкое удообное', 'category': Category.objects.get(pk=3), 'price': 15000},
            {'product_name': 'духовка', 'description': 'продвинутая электроонная', 'category': Category.objects.get(pk=2), 'price': 40000}
        ]

        for product in product_list:
            Product.objects.create(**product)