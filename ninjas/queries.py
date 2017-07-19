import django
from apps.dojo_ninjas.models import Dojo, Ninja 
from apps.book_authors.models import Book, Author

def create_books():
    Book.objects.create(name="C sharp")
    Book.objects.create(name="Java")
    Book.objects.create(name="Python")
    Book.objects.create(name="PHP")
    Book.objects.create(name="Ruby")
    books = Book.objects.all()
    for book in books:
        print book.name

def create_authors():
    Author.objects.create(first_name="Mike")
    Author.objects.create(first_name="Speros")
    Author.objects.create(first_name="John")
    Author.objects.create(first_name="Jaydee")
    Author.objects.create(first_name="Jay")
    authors = Author.objects.all()
    for author in authors:
        print author.first_name

def print_authors():
    authors = Author.objects.all()
    for author in authors:
        print author.first_name
    
def change_fifth(string):
    fifth = Book.objects.last()
    fifth.name = string
    fifth.save()
    print fifth.name

def change_author(new_name):
    fifth = Author.objects.last()
    fifth.first_name = new_name
    fifth.save()
    print fifth.first_name

def assign():
    book1 = Book.objects.first()
    book1.save()
    author = Author.objects.get(id=6)
    author.save()
    book1.authors.add(author)
    book1.save()
    print book1.authors.first().first_name

def list_authors():
    authors = Author.objects.all()
    for author in authors:
        print author.first_name, author.id

def list_books():
    books = Book.objects.all()
    for book in books:
        print book.name, book.id

def assign2():
    fourth_author = Author.objects.get(id=9)
    fourth_author.save()
    books = Book.objects.all()
    for book in books:
        book.authors.add(fourth_author)
        print book.name, book.id, book.authors.first().first_name

def retrieve_authors(book_id):
    book = Book.objects.get(id=book_id)
    book.save()
    authors = book.authors.all()
    for author in authors:
        print author.first_name, author.id

def remove_first(book_id):
    book = Book.objects.get(id=book_id)
    book.save()
    print book.authors.first()
    author = book.authors.first()
    author.delete()
    print book.authors.first()

