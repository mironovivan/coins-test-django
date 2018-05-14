from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin)
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from . import docs
from .models import Payment
from .serializers import PaymentSerializer


class PaymentsViewSet(
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet
):
    __doc__ = docs.PAYMENTS_DOCS
    permission_classes = (AllowAny,)
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
