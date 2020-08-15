from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home.as_view(), name='home'),
    path('invoicedata', views.invoicedata, name='invoicedata'),
    path('generatedinvoice', views.generatedinvoice, name='generatedinvoice'),
    path('charge', views.charge, name='charge'),
    path('emailConsole', views.emailConsole, name='emailConsole'),
    path('dbupdated', views.dbupdated, name='dbupdated'),
    path('clientfilter', views.clientfilter, name='clientfilter'),

]