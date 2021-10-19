from base.views import *
from django.urls import path, re_path

urlpatterns = [
    path('', index, name='home'),
    path('category/', categories),
    path('human/<slug:id>/', human),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]

