from django.db import models
from items.models import inventory
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Quote_item(models.Model):
    item = models.ForeignKey(inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_description}"


    def get_total_item_price(self):
        return self.quantity * self.item.item_price

class Quote202(models.Model):
    quote_number = models.AutoField(primary_key=True)
    start_date = models.DateTimeField(default=timezone.now)
    quote_customer = models.CharField(max_length=200)
    quote_address = models.CharField(max_length=200)
    quote_employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quote_totoal_price = models.CharField(max_length=200)
    quote_items = models.ManyToManyField(Quote_item)

    def __str__(self):
        template = '{0.quote_customer} {0.quote_address} {0.quote_employee} {0.quote_totoal_price} {0.quote_items}'
        return template.format(self) 
