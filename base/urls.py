from base.views import *
from django.urls import path, re_path

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='addpage'),
    path('contacts/', contacts, name='contacts'),
    path('login', login, name='login'),
    path('post/<int:post_id>/', show_post, name='post'),

    path('category/', categories),
    path('human/<slug:id>/', human),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]



