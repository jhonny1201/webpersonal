from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^blog/$', views.blog, name='blog'),
    re_path(r'^blog/post/(?P<pk>\d+)/$', views.blog_detail, name='blog_detail'),
    re_path(r'^blog/category/(?P<pk>\d+)/$', views.blog_category, name='blog_category'),
]