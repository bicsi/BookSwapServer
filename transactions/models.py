from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

from accounts.models import Account
from books.models import Book


class Transaction(models.Model):
    from_account = models.ForeignKey(Account, related_name='%(class)s_from')
    to_account = models.ForeignKey(Account, related_name='%(class)s_to')
    book = models.ForeignKey(Book)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} from {} to {}".format(
            self.book.title,
            self.from_account.username,
            self.to_account.username
        )

admin.site.register(Transaction)
