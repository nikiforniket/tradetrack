from django.contrib import admin

from inventory.models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin): ...
