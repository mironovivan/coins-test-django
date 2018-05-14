from django.db import models

from utils.models import CurrencyField, DefaultCharField


class Account(models.Model):
    id = DefaultCharField(primary_key=True)
    owner = DefaultCharField()
    balance = CurrencyField()
    currency = models.CharField(max_length=3)
