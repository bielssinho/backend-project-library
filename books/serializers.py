from rest_framework import serializers
from copys.models import Copy
from .models import Book

class BooksSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Book:
        new_book = Book.objects.create(**validated_data)

        for i in range(validated_data["quantity"]):
            Copy.objects.create(book=new_book)

        return new_book

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "category",
            "realese_date",
            "synopsis",
            "author",
            "quantity",
        ]
