from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import Menu, Product, ProductCategory


def products(request, pk=None):
    title = "Каталог"
    links_menu = Menu.objects.all()
    products = Product.objects.all().order_by('price')
    basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0 :
            products = Product.objects.all().order_by('price')
            category = {'name': 'Все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.all().filter(category__pk=pk).order_by('price')
        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket':basket
        }
        return render(request, 'mainapp/products.html', context=context)

    same_products = Product.objects.all()[1:2]

    context = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'products': products,
        'basket': basket
    }
    return render(request, 'mainapp/products.html', context=context)
