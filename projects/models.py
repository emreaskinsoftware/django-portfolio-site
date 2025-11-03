from django.db import models

class Project(models.Model):
    """
    Ana Proje Modeli (v2.0)
    """
    title = models.CharField(max_length=200, verbose_name="Proje Başlığı")
    description = models.TextField(verbose_name="Açıklama")
    technology = models.CharField(max_length=200, help_text="Örn: Streamlit, Plotly, Scikit-learn", verbose_name="Teknolojiler")

    # --- v2.0 Değişikliği: 'image' alanı 'cover_image' oldu ---
    cover_image = models.ImageField(
        upload_to='project_covers/', 
        blank=True, null=True, 
        verbose_name="Kapak Resmi (Listeleme için)",
        help_text="Proje listeleme sayfasında (kartta) görünecek ana resim."
    )
    # --- BİTİŞ ---

    video_url = models.URLField(
        max_length=500, blank=True, null=True, 
        verbose_name="Video Gömme (Embed) URL'si",
        help_text="YouTube veya Vimeo'dan 'Embed' (Gömme) linkini buraya yapıştırın."
    )
    github_link = models.URLField(max_length=500, blank=True, null=True)
    live_link = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_technologies_list(self):
        if self.technology:
            return [tech.strip() for tech in self.technology.split(',')]
        return []

    class Meta:
        ordering = ['-created_at']

# --- YENİ EKLENEN MODEL (v2.0 - P2 ÇÖZÜMÜ) ---
class ProjectGalleryImage(models.Model):
    """
    "Kıdemli" (Senior) Galeri Modeli.
    Bu, 'Project' ile "Bire-Çok" (One-to-Many) bir ilişki kurar.
    """
    # "ForeignKey" (Yabancı Anahtar):
    # Bu, bu resmin HANGİ projeye 'ait' olduğunu söyler.
    # 'on_delete=models.CASCADE' -> Ana Proje silinirse, 
    #                              bu resimler de "profesyonelce" (senior) silinir.
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='gallery_images' # Proje'den resimlere 'project.gallery_images.all()' ile erişim
    )

    image = models.ImageField(upload_to='project_gallery/')
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name="Resim Alt Yazısı")

    def __str__(self):
        return f"{self.project.title} - Galeri Resmi"

    class Meta:
        ordering = ['id'] # Yükleme sırasına göre sırala