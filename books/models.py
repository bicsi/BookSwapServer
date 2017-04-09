from __future__ import unicode_literals

from django.contrib import admin
from django.core.validators import (
    MaxValueValidator, MinValueValidator)
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
    goodreads_id = models.BigIntegerField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

admin.site.register(Book)


class Review(models.Model):
    author = models.BigIntegerField()
    book = models.ForeignKey(Book)
    comment = models.TextField(default='')
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ({}*)".format(self.book.title, self.rating)


admin.site.register(Review)
