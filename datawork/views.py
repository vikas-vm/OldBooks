from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages


def home(r):
    data = {
            "books":Books.objects.all(),
            "cat":Category.objects.all(),
            "topic":Topic.objects.all()
            }
    return render(r,'home.html',data)

def insert(r):
    form = BookInsert(r.POST or None, r.FILES or None)
    data = {
            "form":form
    }
    if r.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(r,"data send successfully hogaya")
        else:
            messages.warning(r,"data not nahi nahi hua send")
        return redirect(insert)
    return render(r,'insert.html',data)

def search(r):
    if r.method == "GET":
        searchdata = r.GET.get('search')
        data = {
            "books": Books.objects.filter(book_title__icontains=searchdata),
            "cat": Category.objects.all(),
            "topic": Topic.objects.all()
        }
        return render(r,'home.html',data)
    else:
        return redirect(home)


def category(r,cat_id):
    data = {
        "books": Books.objects.filter(book_topic__topic_category__cat_id=cat_id),
        "cat": Category.objects.all(),
        "topic": Topic.objects.all()
    }
    return render(r,'home.html',data)


def topic(r,topic_id):
    data = {
        "books": Books.objects.filter(book_topic__topic_id=topic_id),
        "cat": Category.objects.all(),
        "topic": Topic.objects.all()
    }
    return render(r,'home.html',data)

def items(r,book_id):
    data = {
        "books": Books.objects.filter(book_id=book_id),
        "cat": Category.objects.all(),
        "topic": Topic.objects.all()
    }
    return render(r,'item.html',data)

