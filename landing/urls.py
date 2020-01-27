from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from landing import views
from telecom.sitemaps import *

sitemaps = {
    'home': HomeSitemap,
    'contacts': ConatctsSitemap,
}


urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^contacts/', views.contacts, name='contacts')
]