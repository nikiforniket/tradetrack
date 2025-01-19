from django.db import models
from django.core.validators import RegexValidator

from common.models import TimestampedModelMixin


class Customer(TimestampedModelMixin):
    name = models.CharField(max_length=100)
    mobile_number = models.PositiveIntegerField(validators=[RegexValidator(
                regex=r'^\d{10}$',
                message="Mobile number must be exactly 10 digits.",
                code="invalid_mobile_number"
            )]
    )
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=7)


    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Order(TimestampedModelMixin):
    product = models.ForeignKey(
        "product.Product", related_name="orders", on_delete=models.RESTRICT
    )
    qty = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.product.name} -> {self.qty}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
