from rest_framework.viewsets import ModelViewSet

from books.library.api.permissions import BaseObjectAccessPermission, ReaderAccessPermission
from books.library.api.serializers import AuthorSerializer, BookSerializer, ReaderSerializer
from books.library.models import Author, Book, Reader

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["author"])
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [BaseObjectAccessPermission]
    tags = ["author"]


@extend_schema(tags=["book"])
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [BaseObjectAccessPermission]
    tags = ["book"]

@extend_schema(tags=["reader"])
class ReaderViewSet(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [ReaderAccessPermission]
    tags = ["reader"]

    # def get_queryset(self):
    #     return Reader.objects.filter(user=self.request.user)
