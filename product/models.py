# -*- coding: utf-8 -*-

from django.db import models
from common.models import TimestampedModelMixin


class Product(TimestampedModelMixin):

    name = models.CharField(max_length=800)
    quality = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} -> {self.quality}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
