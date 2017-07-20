from __future__ import unicode_literals
from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be of valid email format."
        if len(postData['password']) < 8:
            errors['short_password'] = "Password must be 8 characters or more."
        if postData['password'] != postData['confirm_password']:
            errors['password_mismatch'] = "Password and password confirmation must match."
        return errors
    def create_user(self, first, last, email, password):
        try:
            return User.objects.create(first_name=first, last_name=last, email=email, password=password)
        except:
            return None
    def login_validator(self, postData):
        user = User.objects.get(email=postData['email'])
        if user:
            if bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                return user
            else:
                return None
        else:
            return None

class BookManager(models.Manager): 
    def new_book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "You forgot to enter a book."
        if len(postData['author']) < 1:
            errors['author'] = "You forgot to enter an author."
        if len(postData['review']) < 1:
            errors['review'] = "You forgot to enter a review."
        return errors
    
    def new_book_creator(self, postData):
        pass
            

class User(models.Model): 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model): 
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Review(models.Model): 
    rating = models.IntegerField()
    content = models.TextField(max_length=2000)
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






