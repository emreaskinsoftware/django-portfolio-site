# blog/views.py
from django.shortcuts import render
from .models import Post # Veritabanı modelimizi (Post) import et

def post_list_view(request):
    """
    Bu fonksiyon, veritabanındaki TÜM Post nesnelerini çeker
    ve 'context' olarak şablona gönderir.
    """
    # 1. Veritabanı Sorgusu: TÜM gönderileri al
    posts = Post.objects.all() 

    # 2. 'Context' (bağlam) sözlüğü oluştur:
    context = {
        'posts': posts,
    }

    # 3. Veriyi şablona 'render' et (işle)
    #    'blog/post_list.html' adında bir şablon arayacak
    return render(request, 'blog/post_list.html', context)

# blog/views.py
from django.shortcuts import render, get_object_or_404 # 404 için 'get_object_or_404' ekle
from .models import Post 

def post_list_view(request):
    # ... (Bu fonksiyon zaten sizde var)
    posts = Post.objects.all() 
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def post_detail_view(request, pk):
    """
    Bu fonksiyon, veritabanından SADECE 1 'Post' çeker.
    'pk' (primary key), o gönderinin benzersiz ID'sidir.
    """
    # 1. Veritabanı Sorgusu: 'pk' (ID) ile 1 gönderi al
    #    Eğer bulamazsa, otomatik olarak "404 Sayfa Bulunamadı" hatası ver
    post = get_object_or_404(Post, pk=pk)

    # 2. 'Context' (bağlam) sözlüğü oluştur:
    context = {
        'post': post, # 'post'u şablona gönder
    }

    # 3. Veriyi şablona 'render' et (işle)
    return render(request, 'blog/post_detail.html', context)