from django.shortcuts import get_object_or_404
from rest_framework import generics

from accounts import serializers
from accounts.models import Account
from transactions.models import Transaction


class GetCurrentAccountOfBook(generics.RetrieveAPIView):
    def get_object(self):
        seek_id = Transaction.objects \
            .filter(book__id=self.kwargs.get('pk')) \
            .order_by('-created_at') \
            .values('to_account')\
            .first()\
            .get('to_account')
        return get_object_or_404(Account, pk=seek_id)

    serializer_class = serializers.AccountSerializer

