from django.contrib import admin

from order.models import Order, Customer


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): ...

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin): ...