from django.shortcuts import render

from django.views.generic import DetailView

from orders.models import Order


class MyOrderView(DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, querySet=None):
        return Order.objects.filter(is_active=True).first()
