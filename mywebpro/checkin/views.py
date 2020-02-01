from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def checkteachid(request, teacher):
    return HttpResponse("This Subject is teach by %s." % teacher)


def checkcourse(request, sub, amt, stu, abt):
    return HttpResponse("Subject = %s amount = %d studying = %d Absent = %d " % (sub, amt, stu, abt))


def checkin(request, qrCode):
    return HttpResponse("Scan QR CODE Here %s." % qrCode)
