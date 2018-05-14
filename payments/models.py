from django.db import models

from accounts.models import Account
from utils.models import CurrencyField


class Payment(models.Model):
    from_account = models.ForeignKey(
        Account, related_name='from_payments', on_delete='cascade'
    )
    to_account = models.ForeignKey(
        Account, related_name='to_payments', on_delete='cascade'
    )
    amount = CurrencyField()
