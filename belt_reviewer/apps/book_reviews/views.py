from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import User, Book, Review
from django.contrib import messages
import bcrypt


#-----------------------------------------------------------------
#-----------------------------------------------------------------

def index(request):
    
    return render(request, 'book_reviews/index.html')


#-----------------------------------------------------------------
#-----------------------------------------------------------------

def register(request):

    errors = User.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.add_message(request, messages.ERROR, errors[tag])
        return redirect("/")
    else:
        first =  request.POST['first_name']
        last = request.POST['last_name']
        email = request.POST['email']
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
 
        user = User.objects.create_user(first, last, email, hash1)
        print user

        if not user:
            messages.add_message(request, messages.ERROR, "User email already exists.")
            return redirect("/")
        else:
            request.session['user_id'] = user.id
            request.session['first_name'] = first
            return redirect('/success')

#-----------------------------------------------------------------
#-----------------------------------------------------------------


def success(request):
    
    reviews = Review.objects.filter(user_id=request.session['user_id']).order_by("-created_at")

    if len(reviews) > 3:
        reviews = [reviews[0], reviews[1], reviews[2]]

    books = Book.objects.all()

    context = {
        "first_name": request.session['first_name'],
        "recent_reviews": reviews,
        "books": books,
    }
    
    return render(request, 'book_reviews/books.html', context)

#-----------------------------------------------------------------
#-----------------------------------------------------------------

def login(request):

    try:
        user = User.objects.login_validator(request.POST)
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        request.session['email'] = user.email
        request.session['user_id'] = user.id
        return redirect('/success')
    except:
        messages.add_message(request, messages.ERROR, "Invalid login info.")
        return redirect("/")

#-----------------------------------------------------------------
#-----------------------------------------------------------------

def add(request):
    
    books = Book.objects.all()  

    all_authors = []

    for book in books:
        all_authors.append(book.author)

    authors_no_repeats = []

    for author in all_authors:
        if author not in authors_no_repeats:
            authors_no_repeats.append(author)

    print "-"*50
    print authors_no_repeats
    print "-"*50

    context = {
        "authors": authors_no_repeats,
    }

    return render(request, 'book_reviews/add.html', context)


#-----------------------------------------------------------------
#-----------------------------------------------------------------


def make_book_entry(request):

    errors = Book.objects.new_book_validator(request.POST)

    if len(errors):
        for tag, error in errors.iteritems():
            messages.add_message(request, messages.ERROR, errors[tag])
        return redirect("/books/add")
    else:
        title = request.POST['title']
        if request.POST['author']:
            author = request.POST['author']
        else:
            author = request.POST['author_selection']
        review = request.POST['review']
        rating = int(request.POST['rating'])
        try:
            new_book = Book.objects.create(title=title, author=author)
        except:
            messages.add_message(request, messages.ERROR, "That book already has an entry.")

        Review.objects.create(rating=rating, content=review, book=new_book, user_id=request.session['user_id'])
        book_url = '/book/' + str(new_book.id)
        return redirect(book_url)

#-----------------------------------------------------------------
#-----------------------------------------------------------------


def display_book(request, parameter):

    book = Book.objects.get(id=parameter)

    reviews = Review.objects.filter(book=book)

    context = {
        "book": book,
        "book_id": parameter,
        "title": book.title,
        "author": book.author,
        "reviews": reviews,
    }

    return render(request, 'book_reviews/show_book.html', context)


#-----------------------------------------------------------------
#-----------------------------------------------------------------


def logout(request):
    for sesskey in request.session.keys():
        del request.session[sesskey]
    return redirect("/")


#-----------------------------------------------------------------
#-----------------------------------------------------------------


def home(request):
    return redirect("/success")


#-----------------------------------------------------------------
#-----------------------------------------------------------------

def show_user(request, parameter):
    
    user = User.objects.get(id=parameter)
    
    reviews = Review.objects.filter(user__id=user.id)
    review_count = len(reviews)


    context = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "reviews": reviews,
        "review_count": review_count,

    }
    

    return render(request, "book_reviews/user_page.html", context)


#-----------------------------------------------------------------
#-----------------------------------------------------------------


def destroy(request, parameter, book_id):
    review = Review.objects.get(id=parameter)
    review.delete()
    redirect_url = "/book/" + str(book_id)
    return redirect(redirect_url)
    #return redirect('/success')


#-----------------------------------------------------------------
#-----------------------------------------------------------------


def add_review(request):
    
    print "-"*50

    rating = request.POST['rating']
    print "rating: ", rating
    content = request.POST['content']
    print "content: ", content
    #book_id = request.POST['book_id']
    book_id = request.POST['book_id']
    print "request.post.book.id: ",  request.POST['book_id']
    print "-"*50
    book = Book.objects.get(id=book_id)

    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)

    Review.objects.create(rating=rating, content=content, book=book, user=user)

    book_url = '/book/' + str(book_id)
    return redirect(book_url)

