from django.http import HTTPResponse
from django.shortcuts import render


def checkteachid(request, teacher):
    return HTTPResponse("This Subject is teach by %s.", % teacher)


def checkcourse(request, sub, amt, stu, abt):
    return HTTPResponse("Subject = %s amount = %d studying = %d Absent = %d " % (sub, amt, stu, abt))


def checkin(request, qrCode):
    return HTTPResponse("Scan QR CODE Here %s." % qrCode)
