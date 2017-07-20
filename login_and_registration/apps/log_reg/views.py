# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages
import bcrypt


#-----------------------------------------------------------------
#-----------------------------------------------------------------

def index(request):
    
    return render(request, 'log_reg/index.html')


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

        if not user:
            messages.add_message(request, messages.ERROR, "User email already exists.")
            return redirect("/")
        else:
            request.session['first_name'] = first
            request.session['last_name'] = last
            request.session['email'] = email
            request.session['password'] = hash1
            
            return redirect('/success')

#-----------------------------------------------------------------
#-----------------------------------------------------------------


def success(request):

    context = {
        "first_name": request.session['first_name'],
        "last_name": request.session['last_name'],
        "email": request.session['email'],
        "password": request.session['password']
    }
    
    return render(request, 'log_reg/success.html', context)

#-----------------------------------------------------------------
#-----------------------------------------------------------------

def login(request):
    
    user = User.objects.login_validator(request.POST)

    if user:
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        request.session['email'] = user.email
        request.session['password'] = user.password
        return redirect('/success')
    else:
        messages.add_message(request, messages.ERROR, "Invalid login info.")
        return redirect("/")
        


