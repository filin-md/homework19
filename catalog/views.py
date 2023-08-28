from django.shortcuts import render
from django.views.generic import DetailView, ListView

from catalog.models import Product


# Create your views here.

# CReadUD
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


def contacts(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
    return render(request, 'catalog/contacts.html')

