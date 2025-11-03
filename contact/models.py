# contact/models.py
from django.db import models

class Message(models.Model):
    """
    Kullanıcının 'İletişim' formundan gönderdiği mesajları
    veritabanında saklamak için 'profesyonel' (senior) bir model.
    """
    name = models.CharField(max_length=100, verbose_name="Gönderen İsim")
    email = models.EmailField(verbose_name="Gönderen E-posta")
    message = models.TextField(verbose_name="Mesaj İçeriği")

    # 'auto_now_add' -> Mesajın ne zaman geldiğini otomatik kaydeder
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Alınma Tarihi")

    # 'default=False' -> Yeni mesajların 'okunmadı' olarak işaretlenmesi
    is_read = models.BooleanField(default=False, verbose_name="Okundu olarak işaretle")

    def __str__(self):
        # Admin panelinde mesajın 'isim' ile görünmesini sağlar
        return f"Mesaj: {self.name} ({self.email})"

    class Meta:
        # Mesajları en yeniden en eskiye doğru sırala
        ordering = ['-created_at']