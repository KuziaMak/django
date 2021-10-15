from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name="имя",
        unique=True,
    )
    description = models.TextField(
        verbose_name="Описания",
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        verbose_name="имя продукта",
        max_length=128
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True
    )

    shortdesc = models.CharField(
        verbose_name="описания краткое",
        max_length=60,
        blank=True,
    )

    description = models.TextField(
        verbose_name='Описание продукта',
        blank=True
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='цена',
    )

    quantity = models.PositiveIntegerField(
        verbose_name='колеичества на складе',
        default=0
    )

    def __str__(self):
        return f"{self.name} {self.category.name}"


class Menu(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name="имя",
        unique=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name


class Telefon(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name="имя",
        unique=True,
    )

    numbers = models.DecimalField(
        max_digits=8,
        decimal_places=0,
        verbose_name="номер телефона"
    )

    email = models.CharField(
        max_length=100,
        verbose_name="имеил"

    )

    address = models.CharField(
        max_length=100,
        verbose_name="Адрес"
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name