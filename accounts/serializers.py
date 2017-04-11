from rest_framework import serializers

from . import models


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'username',
            'first_name',
            'last_name',
            'gender'
        ]
        model = models.Account