from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('email', views.email, name='email'),
    path('city', views.city, name='city'),
    path('name', views.name, name='name'),
    path('country', views.country, name='country'),
    path('search_company', views.search_company, name='search_company'),
    path('search_email', views.search_email, name='search_email'),
    path('search_city', views.search_city, name='search_city'),
    path('search_name', views.search_name, name='search_name'),
    path('search_country', views.search_country, name='search_country'),
]