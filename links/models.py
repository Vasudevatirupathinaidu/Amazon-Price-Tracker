from django.db import models
from .utils import get_link_data
import uuid

class Link(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    url = models.URLField()
    current_price = models.FloatField(blank=True, null=True)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ("price_difference", "-created")

    def save(self, *args, **kwargs):
        name, price = get_link_data(self.url)
        if self.current_price:
            old_price = self.current_price
            if price != old_price:
                price_diff = price - old_price
                self.price_difference = round(price_diff, 2)
                self.old_price = old_price
            else:
                self.price_difference = 0
                self.old_price = 0

        self.name = name
        self.current_price = price

        super().save(*args, **kwargs)