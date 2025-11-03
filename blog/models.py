# blog/models.py
from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    """
    Veritabanımızdaki 'blog_post' tablosunu temsil eder.
    """
    title = models.CharField(max_length=255)
    
    # "blank=True, null=True" -> Bu alanın 'opsiyonel' (zorunlu değil) olmasını sağlar
    cover_image = models.ImageField(
        upload_to='blog_covers/', 
        blank=True, null=True, 
        verbose_name="Kapak Resmi (Örn: 1200x600px)"
    )

    content = RichTextField(verbose_name="İçerik") 

    # auto_now_add=True -> Nesne ilk oluşturulduğunda o anın tarihini kaydeder
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now=True -> Nesne her GÜNCELLENDİĞİNDE tarihi günceller
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        # Blog gönderilerini en yeniden en eskiye doğru sırala
        ordering = ['-created_at']