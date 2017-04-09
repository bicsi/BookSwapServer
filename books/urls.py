"""BookSwapServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from books import views

urlpatterns = [
    url(r'^$', views.BookListCreate.as_view(), name='book_list'),
    url(r'^(?P<pk>\d+)/$', views.BookRUD.as_view(), name='book_detail'),
    url(r'^(?P<book_pk>\d+)/reviews/$', views.ReviewListCreate.as_view(), name='review_list'),
    url(r'^(?P<book_pk>\d+)/reviews/(?P<pk>\d+)/$', views.ReviewRUD.as_view(), name='review_detail'),
]
