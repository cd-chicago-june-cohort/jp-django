# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import Course

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------


def index(request):
    
    context = {
        "all_courses": Course.objects.all()
    }
    
    return render(request, "courses/index.html", context)

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------


def add(request):
    
    new_name = request.POST['name']
    new_descrip = request.POST['descrip']

    Course.objects.create(name=new_name, description=new_descrip)
    
    return redirect("/")


#-----------------------------------------------------------------------
#-----------------------------------------------------------------------


def delete_page(request, parameter):
    
    course = Course.objects.get(id=parameter)

    context = {
        "course": course
    }

    return render(request, "courses/delete_page.html", context)



#-----------------------------------------------------------------------
#-----------------------------------------------------------------------


def destroy(request, parameter):
    
    course = Course.objects.get(id=parameter)
    course.delete()

    return redirect("/")