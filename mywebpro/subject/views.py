from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def views(request):
    return HttpResponse("views Subject Page")


def add(request):
    return HttpResponse("add Subject Page")


def edit(request):
    return HttpResponse("edit Subject Page")
