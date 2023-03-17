from django.contrib import admin
from django.contrib.admin import register

from books.library.models import Author, Book, Reader

admin.site.register(Author)
admin.site.register(Reader)


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'quantity')
    search_fields = ('title', 'description')



