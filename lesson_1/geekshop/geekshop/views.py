from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product, Telefon


def main(request):
    title = "Магазин"



    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:2]
    context = {
        'title': title,
        "products": products,
    }
    return render(request, "geekshop/index.html", context=context)


def contacts(request):
    title = "Контакты"


    telefon = Telefon.objects.all()[:5]
    context = {
        'title': title,
        'telefon': telefon,
    }
    return render(request, 'geekshop/contact.html', context=context)
