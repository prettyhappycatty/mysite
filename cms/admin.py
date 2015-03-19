from django.contrib import admin

# Register your models here.

from cms.models import Book, Impression

admin.site.register(Book)
admin.site.register(Impression)
