from django.core.management.base import BaseCommand

import json, os

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, Menu, Telefon

JSON_PATH = 'mainapp/jsons'

def load_from_json(file):
    with open(os.path.join(JSON_PATH,file+'.json'), mode="r", encoding='utf8')as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json("categories")

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()


        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            categor_name = product["category"]
            _category = ProductCategory.objects.get(name=categor_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        categories = load_from_json("menu")

        Menu.objects.all().delete()
        for category in categories:
            new_category = Menu(**category)
            new_category.save()

        categories = load_from_json("telefon")

        Telefon.objects.all().delete()
        for category in categories:
            new_category = Telefon(**category)
            new_category.save()

        ShopUser.objects.all().delete()
        super_user = ShopUser.objects.create_superuser('admin','admin@gds.local','123',age=24)
        if super_user:
            print("все ок")