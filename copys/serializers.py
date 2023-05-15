from rest_framework import serializers

from books.serializers import BooksSerializer
from .models import Copy


class CopySerializer(serializers.ModelSerializer):
    book = BooksSerializer()

    class Meta:
        model = Copy
        fields = [
            "id",
            "book",
        ]

        extra_kwargs = {"book": {"read_only": True}}
