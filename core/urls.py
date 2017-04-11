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

from core import views

urlpatterns = [
    url(r'books/(?P<pk>\d+)/current-user/', views.RetrieveCurrentUserOfBook.as_view(), name='current-user'),
    url(r'books/(?P<pk>\d+)/transactions/', views.ListCreateTransactionsOfBook.as_view(), name='list-transactions'),
]
