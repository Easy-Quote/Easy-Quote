from django.db import models

# Create your models here.

class Quote202(models.Model):
    quote_number = models.IntegerField(primary_key=True)
    quote_customer = models.CharField(max_length=200)
    quote_address = models.CharField(max_length=200)
    quote_employee = models.CharField(max_length=200)
    quote_totoal_price = models.CharField(max_length=200)
    quote_items_code = models.CharField(max_length=2000)

    def __str__(self):
        template = '{0.quote_customer} {0.quote_address} {0.quote_employee} {0.quote_totoal_price} {0.quote_items_code}'
        return template.format(self)
    