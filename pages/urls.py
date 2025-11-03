# pages/urls.py

from django.urls import path
from . import views # '.' -> "Bu klasörün içindeki" views.py'yi import et

urlpatterns = [
    # path(URL_deseni, ÇALIŞACAK_FONKSİYON, isim)
    path('', views.home_page_view, name='home'), 
    # '' -> Boş desen (yani /) anasayfa demektir.
]