"""
URL configuration for Curd_State project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Curd_State_App.views import CityListView, CountryListView, StateListView, SubmitListView, ping_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/countries/',CountryListView.as_view(), name='country_list'),
    path('api/states/',StateListView.as_view(), name='state_list'),
    path('api/cities/',CityListView.as_view(), name='city-list'), 
    path('',SubmitListView.as_view(),name= 'index-submit'),
    path('ping/', ping_view, name='ping'),






]
