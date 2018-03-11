# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
# def index(req):
#     return render(req, 'blogs_app/index.html')
# def new(req):
#     return render(req, 'blogs_app/new.html')
# def create(req):
#     return redirect('blogs_app/')
# def show(req):
#     return render(req, 'blogs_app/show.html')
# def edit(req):
#     return render(req, 'blogs_app/edit.html')
# def destroy(req):
#     return redirect(req, '/')

def index(req):
    response = "placeholder for some stuff"
    return HttpResponse(response)

def new(req):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(req):
    return redirect('/')

def show(req, number):
    response = 'placeholder to display blog {}'.format(number)
    return HttpResponse(response)

def edit(req, number):
    response = "placeholder to edit blog {}".format(number)
    return HttpResponse(response)

def destroy(req, number):
    return redirect('/')