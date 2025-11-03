# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # /contact/ adresinin kök dizini ('')
    path('', views.contact_view, name='contact'),
]