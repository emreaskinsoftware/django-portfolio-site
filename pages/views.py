# pages/views.py

from django.shortcuts import render # <-- HttpResponse'a artık gerek yok

# Bu, Anasayfa (home) için 'view' fonksiyonumuzdur
def home_page_view(request):
    
    # render(request, HANGİ_ŞABLON, HANGİ_VERİ (opsiyonel))
    return render(request, 'home.html')