from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'id',
            'title',
            'author',
            'genre',
            'short_description',
            'created_at',
        ]
        model = models.Book
