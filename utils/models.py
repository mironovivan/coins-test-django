from django.db import models


class DefaultCharField(models.CharField):
    MAX_LENGTH = 255

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', self.MAX_LENGTH)
        super().__init__(*args, **kwargs)


class CurrencyField(models.DecimalField):
    def __init__(self, max_digits=9, decimal_places=2, **kwargs):
        super().__init__(
            max_digits=max_digits, decimal_places=decimal_places, **kwargs
        )
