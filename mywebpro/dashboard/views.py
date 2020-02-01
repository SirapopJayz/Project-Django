from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboard(req):
    return HttpResponse("Dashboard Page")


def searchDailyCheckIn(req, semisterId):
    return HttpResponse("CheckIN OF Semister %s" % semisterId)
