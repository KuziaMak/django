from django.conf import settings
from django.db import models

from mainapp.models import Product

class BasketQuerySet(models.QuerySet):
    def delete(self,*args,**kwargs):
        for obj in self:
            obj.products.quantity += obj.quantity
            obj.products.save()
        super(BasketQuerySet,self).delete()



class Basket(models.Model):
    objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='колеичество',
        default=0,
    )
    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )
    # is_active = models.BooleanField(verbose_name='активна', default=True)

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()


    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user)

    @property
    def product_cost(self):
        return self.product.price * self.quantity    \


    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return _total_quantity

    @property
    def total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _items)))
        return _total_cost


    def delete(self):
        self.product.quantity += self.quantity
        self.product.save()
        super(Basket,self).delete()

    def save(self,*args,**kwargs):
        if self.pk:
            self.product.quantity -= self.pk.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args,**kwargs)