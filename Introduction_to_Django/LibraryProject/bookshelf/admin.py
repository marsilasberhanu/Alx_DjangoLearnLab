from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Columns to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right sidebar for easier filtering
    list_filter = ('author', 'publication_year')

    # Enable search functionality on the fields below
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
