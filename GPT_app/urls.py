from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index'),
    path('p2', views.p2, name='p2'),
    path('p3', views.p3, name='p3'),
    path('p4', views.p4, name='p4'),
]
