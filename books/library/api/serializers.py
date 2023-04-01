from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.library.models import Author, Book, Reader


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = [
            'id',
            'first_name',
            'first_name',
            'photo'
        ]

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields = [
            'id',
            'author',
            'title',
            'description',
            'quantity',
            'total_page',
        ]

class ReaderSerializer(serializers.ModelSerializer):
    def validate(self, data):
        data['phone_number'] = data.get('phone_number')[1:]
        self.__validate_phone_number(data.get('phone_number'))
        self.__validate_count_books(data.get('active_books'))
        return super().validate(data)
    @staticmethod
    def __validate_phone_number(number: str):
        if not number.startswith('7'):
            raise ValidationError('Invalid phone number, start with +7')
        if len(number) != 11:
            print(len(number))
            raise ValidationError('Invalid len phone number')
    @staticmethod
    def __validate_count_books(books: dict):
        if len(books) > 3:
            raise ValidationError('max count books 3')

    def create(self, validated_data):
        # validate active books
        books = validated_data.get("active_books", [])
        for book in books:
            if book.count <= 0:
                raise ValidationError(
                    "You can't assign books if they are not available"
                )
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # validate active books
        books = validated_data.get("active_books", [])
        for book in books:
            if (
                    book.count <= 0
                    and not instance.active_books.filter(id=book.id).exists()
            ):
                raise ValidationError(
                    "You can't assign books if they are not available"
                )
        return super().update(instance, validated_data)


    class Meta:
        model= Reader
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'status',
            'active_books'
        ]
