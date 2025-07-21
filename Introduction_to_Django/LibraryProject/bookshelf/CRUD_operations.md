
# Create Book
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book


# Retrieve Book

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title          
book.author         
book.publication_year  

# Update Book Title

from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title 

# Delete Book

from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all() 

