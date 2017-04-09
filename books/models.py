from __future__ import unicode_literals

from django.contrib import admin
from django.db import models


class BookGenre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


admin.site.register(BookGenre)


class BookAuthor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name


admin.site.register(BookAuthor)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(BookAuthor, default=None)
    genre = models.ForeignKey(BookGenre, default=None)
    short_description = models.TextField()
    goodreads_id = models.IntegerField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


admin.site.register(Book)
