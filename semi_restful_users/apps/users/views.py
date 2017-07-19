# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import User

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def index(request):

    context = {
        "all_users": User.objects.all(),
    }

    return render(request, 'users/index.html', context)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def new(request):
    return render(request, 'users/new.html')

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def create(request):

    first = request.POST['first_name']
    last = request.POST['last_name']
    mail = request.POST['email']
    print "-"*50
    print first, last, mail
    print "-"*50

    new_user = User.objects.create(first_name=first, last_name=last, email=mail)

    url = "/users/show/" + str(new_user.id)

    return redirect(url)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def show(request, parameter):
    
    user = User.objects.get(id=parameter)

    context = {
        "id": parameter,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "created_at": user.created_at,
    }

    return render(request, 'users/show.html', context)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def edit(request, parameter):

    user = User.objects.get(id=parameter)

    context = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "id": user.id,
    }

    return render(request, 'users/edit.html', context)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def update(request, parameter):
    
    user = User.objects.get(id=parameter)
    
    new_first = request.POST['first_name']
    new_last = request.POST['last_name']
    new_email = request.POST['email']

    user.first_name = new_first
    user.last_name = new_last
    user.email = new_email
    user.save()

    url = "/users/show/" + str(user.id)

    return redirect(url)

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

def destroy(request, parameter):
    
    user = User.objects.get(id=parameter)

    user.delete()

    return redirect("/users")