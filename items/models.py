from django.db import models
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

class inventory(models.Model):
    item_code = models.CharField(max_length=200, primary_key=True)
    item_description = models.CharField(max_length=200)
    item_price = models.CharField(max_length=200)

    def __str__(self):
        template = '{0.item_code} {0.item_description} {0.item_price}'
        return template.format(self)
