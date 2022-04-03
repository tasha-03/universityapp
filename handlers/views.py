from django.shortcuts import render

from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseGone, HttpResponseNotAllowed, HttpResponseNotFound, HttpResponseNotModified, HttpResponseServerError
from django.shortcuts import render

def m304(request):
    return HttpResponseNotModified("<h2>Not Modified</h2>")

def m400(request, exception):
    return HttpResponseBadRequest("<h2>Bad Request</h2>")

def m403(request, exception):
    return HttpResponseForbidden("<h2>Forbidden</h2>")

def m404(request, exception):
    return HttpResponseNotFound("<h2>Not Found</h2>")

def m405(request):
    return HttpResponseNotAllowed("<h2>Not Allowed</h2>")

def m410(request):
    return HttpResponseGone("<h2>Gone</h2>")

def m500(request):
    return HttpResponseServerError("<h2>Internal Server Error</h2>")