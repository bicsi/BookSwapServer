from django.shortcuts import get_object_or_404
from rest_framework import generics

from accounts.models import Account
from accounts.serializers import AccountSerializer
from books.models import Book
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer


class RetrieveCurrentUserOfBook(generics.RetrieveAPIView):
    def get_object(self):
        seek_id = Transaction.objects \
            .filter(book__id=self.kwargs.get('pk')) \
            .order_by('-created_at') \
            .values('to_account') \
            .first() \
            .get('to_account__')
        return get_object_or_404(Account, pk=seek_id)

    serializer_class = AccountSerializer


class ListCreateTransactionsOfBook(generics.ListCreateAPIView):
    def get_queryset(self):
        return Transaction.objects.filter(book__id=self.kwargs.get('pk'))

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get('pk'))
        serializer.save(book=book)

    serializer_class = TransactionSerializer
