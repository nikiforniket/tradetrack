# -*- coding: utf-8 -*-

from django.db import models

from common.models import TimestampedModelMixin


class Inventory(TimestampedModelMixin):

    product = models.ForeignKey(
        "product.Product", related_name="inventories", on_delete=models.RESTRICT
    )
    qty = models.PositiveIntegerField()
    cost_price = models.DecimalField(max_digits=15, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.product.name} -> {self.qty}"

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventories"
