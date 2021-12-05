from django.core.management.base import BaseCommand
from django.db.models import F,Q, When, Case, DecimalField, IntegerField
from  datetime import timedelta

from ordersapp.models import OrderItem


class Command(BaseCommand):
    def handle(self, *args, **options):
        ACTION_1 = 1
        ACTION_2 = 2
        ACTION_EXPIRED = 3

        action_1__time_delta = timedelta(hours=12)
        action_2__time_delta = timedelta(days=1)

        action_1__disconunt = 0.3
        action_2__disconunt = 0.15
        action_expired__disconunt = 0.05

        action_1__condition = Q(order__update__lte=F('order__created') + action_1__time_delta)
        action_2__condition = Q(order__updated__gt=F('order__created') + \
                                                   action_1__time_delta) & \
                              Q(order__updated__lte=F('order__created') + \
                                                    action_2__time_delta)
        action_expired__condition = Q(order__update__gt=F('order__created') + action_2__time_delta)

        action_1__order = When(action_1__condition, then=ACTION_1)
        action_2__order = When(action_2__condition, then=ACTION_2)
        action_expired__order = When(action_expired__condition, then=ACTION_EXPIRED)

        action_1__pirce = When(action_1__condition, then=F('product__price') * F('qubntity')* action_1__disconunt)
        action_2__pirce = When(action_2__condition, then=F('product__price') * F('qubntity')* action_2__disconunt)
        action_expired__pirce = When(action_expired__condition,
                                     then=F('product__price') * F('qubntity')* action_expired__disconunt)

        test_orders = OrderItem.objects.annotate(
            action_order=Case(
                action_1__order,
                action_2__order,
                action_expired__order,
                output_field=IntegerField(),
            )
        ).annotate(
            total_price=Case(
                action_1__pirce,
                action_2__pirce,
                action_expired__pirce,
                output_field=DecimalField()
            )
        ).order_by('action_order', 'total_price').select_related()

        for orderitem in test_orders:
            print(f'{orderitem.action_order:2}: заказ №{orderitem.pk:3}:'
                  f'{orderitem.product.name:15}: скидка {abs(orderitem.total_price):6.2f} руб. |'
                  f'{orderitem.order.updated - orderitem.order.created}')