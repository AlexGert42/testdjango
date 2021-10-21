from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here.
from base.models import Human



menu = [
    {'title': 'Base', 'url': 'home'},
    {'title': 'About', 'url': 'about'},
    {'title': 'Contacts', 'url': 'contacts'},
    {'title': 'Login', 'url': 'login'},
]


def index(request):
    post_date = Human.objects.all()
    context = {
        'posts': post_date,
        'title': 'Base Page',
        'menu': menu
    }
    return render(request, 'base/index.html', context=context)


def about(request):
    context = {
        'title': 'About',
        'menu': menu
    }
    return render(request, 'base/about.html', context=context)


def addpage(request):
    return render(request, 'base/addpage.html')


def contacts(request):
    return render(request, 'base/contacts.html')


def login(request):
    return render(request, 'base/login.html')


def show_post(request, post_id):
    return HttpResponse(f"Page Post {post_id}")


######################################################
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
