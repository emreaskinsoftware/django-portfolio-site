# projects/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # /projects/ adresinin kök dizini ('')
    path('', views.project_list_view, name='project_list'),
    # /projects/<pk>/ -> (örn: /projects/1/)
    # <int:pk> -> URL'deki sayıyı (integer) yakalar ve 'pk' adıyla
    #             view fonksiyonuna (project_detail_view) gönderir.
    path('<int:pk>/', views.project_detail_view, name='project_detail'),
]