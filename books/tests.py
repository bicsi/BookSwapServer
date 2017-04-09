# Create your tests here.

from django.test import TestCase
from rest_framework.renderers import JSONRenderer

from models import Book, BookGenre, BookAuthor
from serializers import BookSerializer


class AddBookTest(TestCase):
    def setUp(self):
        genre = BookGenre.objects.create(name="Action")
        author = BookAuthor.objects.create(first_name="Ala", last_name="Bala")

        for i in range(100):
            Book.objects.create(
                title="Test book #" + str(i),
                short_description="Short description for book #" + str(i),
                genre=genre,
                author=author,
            )

    def testAllBooksInserted(self):
        for i in range(100):
            Book.objects.get(title="Test book #" + str(i))

    def testBookSerialized(self):
        book = Book.objects.get(title="Test book #0")
        serializer = BookSerializer(book)
        jsonString = JSONRenderer().render(serializer.data)
        print str(jsonString)
