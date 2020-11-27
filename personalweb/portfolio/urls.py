from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^portfolio/$', views.view_portfolio, name='portfolio'),
    re_path(r'^portfolio/(?P<pk>\d+)/$', views.portfolio_detail, name='portfolio_detail'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)