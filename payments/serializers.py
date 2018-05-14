from django.db import transaction
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from accounts.serializers import AccountSerializer
from .consts import ERROR_INSUFFICIENT_FUNDS
from .models import Payment


class PaymentSerializer(ModelSerializer):
    from_account_detail = AccountSerializer(
        source='from_account', read_only=True
    )
    to_account_detail = AccountSerializer(source='to_account', read_only=True)

    class Meta:
        model = Payment
        fields = (
            'id', 'from_account', 'to_account', 'amount',
            'from_account_detail', 'to_account_detail'
        )

    def validate(self, attrs):
        """
        Validates the source data.
        Checks if from account has sufficient funds on its balance.
        :param attrs: Source data to validate.
        :return: Validated data.
        """
        if attrs['from_account'].balance < attrs['amount']:
            raise ValidationError(
                ERROR_INSUFFICIENT_FUNDS.format(attrs['from_account'].owner)
            )

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        """
        Creates a payment and moved funds from one account to another.
        :param validated_data: Validated input for creation of a payment.
        :return: Target payment.
        """
        payment = super().create(validated_data)
        from_account = validated_data['from_account']
        from_account.balance -= validated_data['amount']
        from_account.save()
        to_account = validated_data['to_account']
        to_account.balance += validated_data['amount']
        to_account.save()
        return payment
