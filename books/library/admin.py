from books.library.models import Author, Book, Reader
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'photo', 'create_data', 'edit_data')
    list_filter = ('create_data', 'edit_data')


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'author', 'title', 'description', 'quantity', 'total_page', 'create_data', 'edit_data', 'author_link')
    list_filter = ('author', 'quantity', 'create_data', 'edit_data')

    def author_link(self, obj):
        url = reverse('admin:library_author_change', args=[obj.author_id])
        return format_html("<a href='{}'>{}</a>", url, obj.author)

    def make_book_unavailable(self, request, queryset):
        queryset.update(available_copies=0)

    make_book_unavailable.short_description = "Отметить выбранные книги как недоступные"

    actions = [make_book_unavailable]


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone_number', 'status', 'edit_data')
    list_filter = ('status', 'edit_data')
    list_display_links = ('phone_number',)

    def make_active(self, request, queryset):
        queryset.update(status=True)

    make_active.short_description = "Активировать выбранных читателей"

    # экшен для изменения статуса неактивности читателя
    def make_inactive(self, request, queryset):
        queryset.update(status=False)

    make_inactive.short_description = "Деактивировать выбранных читателей"

    def delete_all_books(self, request, queryset):
        for obj in queryset:
            obj.books.clear()

    delete_all_books.short_description = "Удалить все книги у выбранных пользователей"

    actions = [make_active, make_inactive, delete_all_books]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Reader, ReaderAdmin)




