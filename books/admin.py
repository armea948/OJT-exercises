from django.contrib import admin

from models import Author, Book, Publisher

class AuthorAdmin(admin.ModelAdmin):
    fields = ['email', 'first_name', 'last_name']
    list_display = ['email']
    search_fields = ['first_name', 'last_name']


class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'authors', 'publisher']}),
        ('Date information', {
        'fields': ['publication_date'],
        'classes': ['collapse'],
        }),
    ]
    list_display = ['title', 'publisher', 'publication_date', 'was_published_recently'] #, 'authors']
    list_filter = ['publication_date']
    search_fields = ['title']
    filter_horizontal = ['authors']

class BookInline(admin.StackedInline):
    model = Book
    extra = 3

class PublisherAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    search_fields = ['name','city', 'country', 'website']
    list_display = ['name', 'city', 'country', 'website']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher, PublisherAdmin)
