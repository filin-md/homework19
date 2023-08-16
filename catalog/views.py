from django.shortcuts import render

# Create your views here.


def home(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
    return render(request, 'catalog/home.html')

def contacts(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
    return render(request, 'catalog/contacts.html')
