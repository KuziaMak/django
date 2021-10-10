from django.shortcuts import render
from .models import Menu

def products(request):
    title = "Каталог"
    links_menu = Menu.objects.all()
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html',context=context)
# Create your views here.
