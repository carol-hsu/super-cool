"""super_cool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
import super_cool.bewsito.views as view
from config import ApplicationConfig
import django

urlpatterns = [
    url(r'^bewsito/', view.mainpage),
    url(r'^js/(?P<path>.*)$', django.views.static.serve,
        {'document_root': ApplicationConfig.get_source('js')}, name='JS'),

    url(r'^css/(?P<path>.*)$', django.views.static.serve,
        {'document_root': ApplicationConfig.get_source('css')}, name='CSS'),

    url(r'^images/(?P<path>.*)$', django.views.static.serve,
        {'document_root': ApplicationConfig.get_source('image')}, name='IMG'),
]
