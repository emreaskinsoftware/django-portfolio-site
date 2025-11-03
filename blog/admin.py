# blog/admin.py
from django.contrib import admin
from .models import Post

# "Kıdemli" (Senior) Admin Tanımı (P2 Çözümü):
# Bu sınıf, Django Admin'in 'Post' modelini nasıl
# "profesyonelce" (senior) göstereceğini özelleştirir.
class PostAdmin(admin.ModelAdmin):
    # Admin listesinde hangi sütunlar görünsün?
    list_display = ('title', 'created_at', 'updated_at')
    # Hangi sütunlara göre filtreleme yapılabilsin?
    list_filter = ('created_at',)
    # Hangi sütunlarda arama yapılabilsin?
    search_fields = ('title', 'content')

    # 'fields' -> Admin panelindeki "formun" sırasını ve
    #             görünümünü "profesyonelce" (senior) kontrol eder.
    # Bu, 'cover_image'ın 'content' (İçerik) alanından ÖNCE
    # gelmesini sağlar (daha iyi UX).
    fields = ('title', 'cover_image', 'content', 'created_at', 'updated_at')

    # 'readonly_fields' -> 'created_at' gibi 'auto_now' alanlarının
    #                      "değiştirilemez" (non-editable) olmasını sağlar.
    readonly_fields = ('created_at', 'updated_at')

# 'Post' modelini, 'PostAdmin' ayarlarıyla admin paneline kaydet
admin.site.register(Post, PostAdmin)