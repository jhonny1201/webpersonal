from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^contact/$', views.contact, name='contact'),
]