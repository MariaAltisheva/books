from django.contrib import admin
from django.contrib.admin import register
from django.shortcuts import redirect
from django.urls import reverse
from books.library.models import Author, Book, Reader
from django.core.exceptions import ValidationError
from django.contrib import messages
admin.site.register(Author)
# admin.site.register(Reader)



def url_to_edit_object(obj):
  url = reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id] )
  return u'<a href="%s">Edit %s</a>' % (url,  obj.__unicode__())
# def url_to_edit_object(obj):
#     url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
#     return u'<a href="%s">Edit %s</a>' % (url, obj)

@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'quantity')
    search_fields = ('title', 'description')


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if len(form.cleaned_data["active_books"]) > 3:
            from django.contrib import messages
            messages.add_message(request, messages.INFO,'Maximum count books to save must 3')
            raise ValidationError('Maximum count books to save must 3')
        else:
            super().save_model(request, obj, form, change)




