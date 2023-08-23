from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def home(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
    return render(request, 'catalog/contacts.html')


def product(request):
    products_list = Product.objects.all()[0]
    context = {
        'object': products_list
    }
    return render(request, 'catalog/product.html', context)