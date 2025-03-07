from uuid import uuid4

from django.db import models
from django.core.validators import MinValueValidator 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    @property
    def total_price(self):
        return round(sum([item.item_ref.quantity * item.price for item in self.item_set.all()]) / 100, 2)


class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    item_ref_id = models.PositiveIntegerField()
    item_ref = GenericForeignKey("content_type", "item_ref_id")
    # In cents
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)])