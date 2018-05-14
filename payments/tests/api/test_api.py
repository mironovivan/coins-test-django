from decimal import Decimal

from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import Account
from payments.consts import ERROR_INSUFFICIENT_FUNDS
from payments.models import Payment


class TestAccounts(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.client = cls.client_class()

    def setUp(self):
        self.from_account = mommy.make(
            Account, id='bob123', owner='bob', balance=Decimal(100),
            currency='PHP'
        )
        self.to_account = mommy.make(
            Account, id='alice456', owner='alice', balance=Decimal('0.01'),
            currency='PHP'
        )
        self.payments_list_url = reverse('payments:payment-list')

    def test_successful_payment(self):
        """
        Check the case of successful payment.
        """
        # Make payment.
        amount = 10
        data = {
            'from_account': self.from_account.id,
            'to_account': self.to_account.id,
            'amount': amount,
        }
        response = self.client.post(
            self.payments_list_url, data=data, format='json'
        )
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED, response.data
        )
        payment_id = response.data['id']
        self.assertTrue(Payment.objects.filter(pk=payment_id).exists())

        # Make sure that payments is available through readonly endpoints.
        response = self.client.get(self.payments_list_url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, response.data
        )
        self.assertEqual(len(response.data), 1)

        detail_url = reverse('payments:payment-detail', args=[payment_id])
        response = self.client.get(detail_url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, response.data
        )
        self.assertEqual(response.data['from_account'], self.from_account.id)
        self.assertEqual(response.data['to_account'], self.to_account.id)
        self.assertEqual(Decimal(response.data['amount']), amount)

        # Make sure that funds are moved from "bob123" to "alice456".
        original_amount = self.from_account.balance
        self.from_account.refresh_from_db()
        self.assertEqual(self.from_account.balance, original_amount - amount)
        original_amount = self.to_account.balance
        self.to_account.refresh_from_db()
        self.assertEqual(self.to_account.balance, original_amount + amount)

    def test_insufficient_funds(self):
        """
        Check the case of insufficient funds.
        """
        data = {
            'from_account': self.from_account.id,
            'to_account': self.to_account.id,
            'amount': '100.01',
        }
        response = self.client.post(
            self.payments_list_url, data=data, format='json'
        )
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST, response.data
        )
        self.assertIn(
            ERROR_INSUFFICIENT_FUNDS.format(self.from_account.owner),
            response.data['non_field_errors']
        )
