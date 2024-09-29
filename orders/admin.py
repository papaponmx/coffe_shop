from django.contrib import admin

from orders.models import Order, OrderProuct


class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProuct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInlineAdmin]


admin.site.register(Order, OrderAdmin)
