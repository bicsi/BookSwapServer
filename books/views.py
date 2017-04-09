# Create your views here
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers, models


class BookList(APIView):
    def get(self, request, format=None):
        courses = models.Book.objects.all()
        serializer = serializers.BookSerializer(
            courses, many=True)
        return Response(serializer.data)


class CreateBook(APIView):
    def post(self, request, format=None):
        serializer = serializers.BookSerializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)
