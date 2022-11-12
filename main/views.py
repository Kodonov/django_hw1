

from django.shortcuts import HttpResponse
from datetime import datetime, date


def hello(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def goodby(request):
    if request.method == 'GET':
        return HttpResponse("Goodby user!")


def now_date(request):

    if request.method == 'GET':
        return HttpResponse(datetime.now())


