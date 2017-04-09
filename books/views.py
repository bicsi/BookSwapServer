# Create your views here
from django.shortcuts import get_object_or_404
from rest_framework import generics

from . import serializers, models


class BookListCreate(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class ReviewListCreate(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        return self.queryset.filter(book=self.kwargs.get('book_pk'))

    def perform_create(self, serializer):
        book = get_object_or_404(models.Book, pk=self.kwargs.get('book_pk'))
        serializer.save(book=book)


class ReviewRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            book_id=self.kwargs.get('book_pk'),
            pk=self.kwargs.get('pk')
        )