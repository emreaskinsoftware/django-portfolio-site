# contact/admin.py
from django.contrib import admin
from .models import Message # 'Message' modelimizi import et

# "Kıdemli" (Senior) Admin Tanımı:
# Sadece 'kayıt' (register) etmekle kalmayıp,
# 'admin' panelinin GÖRÜNÜMÜNÜ de özelleştiriyoruz.
class MessageAdmin(admin.ModelAdmin):
    # Listede hangi sütunlar görünsün?
    list_display = ('name', 'email', 'created_at', 'is_read')
    # Hangi sütunlara göre filtreleme yapılabilsin?
    list_filter = ('is_read', 'created_at')
    # Hangi sütunlarda arama yapılabilsin?
    search_fields = ('name', 'email', 'message')

# 'Message' modelini, 'MessageAdmin' ayarlarıyla admin paneline kaydet
admin.site.register(Message, MessageAdmin)