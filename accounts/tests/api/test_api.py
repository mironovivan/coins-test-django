from decimal import Decimal

from django.urls import reverse
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import Account


class TestAccounts(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.client = cls.client_class()

    def setUp(self):
        self.account = mommy.make(
            Account, id='bob123', owner='bob', balance=Decimal(100),
            currency='PHP'
        )
        mommy.make(
            Account, id='alice456', owner='alice', balance=Decimal('0.01'),
            currency='PHP'
        )

    def test_list(self):
        """
        Check accounts list endpoint.
        """
        url = reverse('accounts:account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_detail(self):
        """
        Check accounts detail endpoint.
        """
        url = reverse('accounts:account-detail', args=[self.account.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.account.owner, response.data['owner'])
        self.assertEqual(
            self.account.balance, Decimal(response.data['balance'])
        )
        self.assertEqual(self.account.currency, response.data['currency'])
