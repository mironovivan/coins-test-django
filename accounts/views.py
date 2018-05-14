from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from . import docs
from .models import Account
from .serializers import AccountSerializer


class AccountsViewSet(ReadOnlyModelViewSet):
    __doc__ = docs.ACCOUNTS_DOCS
    permission_classes = (AllowAny,)
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
