from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product, Telefon


def main(request):
    title = "Магазин"
    basket = Basket.objects.filter(user=request.user)


    products = Product.objects.all()[:5]
    context = {
        'title': title,
        "products": products,
        'basket': basket,
    }
    return render(request, "geekshop/index.html", context=context)


def contacts(request):
    title = "Контакты"
    basket = Basket.objects.filter(user=request.user)


    telefon = Telefon.objects.all()[:5]
    context = {
        'title': title,
        'telefon': telefon,
        'basket': basket,
    }
    return render(request, 'geekshop/contact.html', context=context)
