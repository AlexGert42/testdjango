from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return HttpResponse('Base Page')


def categories(request):
    if (request.GET):
        print('Request', request.GET)
    return HttpResponse('<h1>Category Page</h1>')


def human(request, id):
    return HttpResponse(f'<h3>Human Page</h3><p>{id}</p>')


def archive(request, year):
    if int(year) > 2021:
        return redirect('home', permanent=True)

    return HttpResponse(f'<h1>Archive for years</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page Not Found</h1>')
