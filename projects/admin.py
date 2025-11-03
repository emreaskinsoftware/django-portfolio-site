# projects/admin.py (YENİDEN YAZILDI - v2.0 MİMARİSİ)

from django.contrib import admin
from .models import Project, ProjectGalleryImage # <-- İKİ MODELİ DE IMPORT ET

# --- "Kıdemli" (Senior) Admin UX (P2 ÇÖZÜMÜ) ---
# Bu sınıf, 'Project' admin sayfasının *içinde*
# "iç içe" (inline) bir 'Galeri' formu oluşturur.
class ProjectGalleryImageInline(admin.TabularInline):
    model = ProjectGalleryImage
    extra = 1 # Varsayılan olarak 1 boş "Resim Yükle" alanı göster
    fields = ('image', 'caption')
    verbose_name = "Galeri Resmi"
    verbose_name_plural = "Proje Galerisi (Sınırsız Resim Ekleyebilirsiniz)"
# --- BİTİŞ ---


# "Kıdemli" (Senior) Admin Tanımı:
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description', 'technology')

    # Formun sırasını "profesyonelce" (senior) düzenle
    fields = (
        'title', 'description', 'technology', 
        'cover_image', # <-- 'image' -> 'cover_image' olarak güncellendi
        'video_url', 
        'github_link', 'live_link',
        'created_at'
    )
    readonly_fields = ('created_at',)

    # --- YENİ EKLENEN SATIR (P2 ÇÖZÜMÜ) ---
    # 'ProjectGalleryImageInline' sınıfını, bu admin sayfasına "iç içe" dahil et
    inlines = [ProjectGalleryImageInline]
    # --- BİTİŞ ---

# 'Project' modelini, 'ProjectAdmin' ayarlarıyla kaydet
admin.site.register(Project, ProjectAdmin)

# Not: 'ProjectGalleryImage'i ayrıca register ETMEYİN.
# O, zaten 'ProjectAdmin'in 'içinde' (inline) yönetiliyor.