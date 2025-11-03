# projects/views.py
from django.shortcuts import render
from .models import Project # Veritabanı modelimizi import et

def project_list_view(request):
    """
    Bu fonksiyon, veritabanındaki TÜM Project nesnelerini çeker
    ve 'context' olarak şablona gönderir.
    """
    # 1. Veritabanı Sorgusu: TÜM projeleri al
    projects = Project.objects.all()

    # 2. 'Context' (bağlam) sözlüğü oluştur:
    #    HTML şablonumuzun 'projects' adıyla bu veriye erişmesini sağlar
    context = {
        'projects': projects,
    }

    # 3. Veriyi şablona 'render' et (işle)
    #    'projects/project_list.html' adında bir şablon arayacak
    return render(request, 'projects/project_list.html', context)

def project_detail_view(request, pk):
    """
    Bu fonksiyon, veritabanından SADECE 1 proje çeker.
    'pk' (primary key), o projenin benzersiz ID'sidir (1, 2, 3...).
    """
    try:
        # 1. Veritabanı Sorgusu: 'pk' (ID) ile 1 proje al
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        # (Profesyonel Dokunuş: Eğer o ID'de proje yoksa 404 hatası ver)
        from django.http import Http404
        raise Http404("Proje bulunamadı.")

    # 2. 'Context' (bağlam) sözlüğü oluştur:
    context = {
        'project': project, # 'project'i şablona gönder
    }

    # 3. Veriyi şablona 'render' et (işle)
    return render(request, 'projects/project_detail.html', context)