from rest_framework.viewsets import ModelViewSet

from books.library.api.serializers import AuthorSerializer, BookSerializer, ReaderSerializer
from books.library.models import Author, Book, Reader


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
