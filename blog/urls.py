# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # /blog/ adresinin kök dizini ('')
    path('', views.post_list_view, name='post_list'),
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
]