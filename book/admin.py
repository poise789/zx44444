from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book,Review
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title', 'description']
    list_editable = ('description',)
admin.site.register(Book,BookAdmin)
admin.site.register(Review)