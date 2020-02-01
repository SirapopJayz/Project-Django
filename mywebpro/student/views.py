from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def views(request):
    return HttpResponse("views student Page")


def add(request):
    return HttpResponse("add Student Page")


def edit(request):
    return HttpResponse("edit Student Page")
