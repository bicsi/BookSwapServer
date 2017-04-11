from rest_framework import serializers

from . import models


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'from_account',
            'to_account',
            'book',
            'created_at'
        ]
        model = models.Transaction