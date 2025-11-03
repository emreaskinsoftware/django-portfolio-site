# 🚀 Full-Stack Django Portfolyo Sitesi (Proje 5)

Bu proje, "kıdemli" (senior) yazılım mimarisi prensipleri (SRP, DRY, MVT) kullanılarak sıfırdan inşa edilmiş, "profesyonel" (professional) ve "tam yığın" (full-stack) bir portfolyo web sitesidir.

**Canlı Demo Linki:** `[Henüz Dağıtılmadı - Yakında Eklenecek]`

---

## ✨ "Kıdemli" (Senior) Mimari ve "Profesyonel" (Professional) Özellikler

Bu proje, "çalışan" bir prototipten öte, "sürdürülebilir" (maintainable) ve "güvenli" (secure) bir yazılım ürünü olarak tasarlanmıştır:

### 1. Modüler Mimari (SRP & DRY Tasarım Desenleri)
* **SRP (Tek Sorumluluk Prensibi):** Proje, her biri kendi "profesyonel" (senior) sorumluluğuna sahip **5 ayrı Django "App" (Uygulama)** modülüne bölünmüştür: `pages`, `projects`, `blog`, `contact` ve `ratelimit`.
* **DRY (Kendini Tekrar Etme):** Sitedeki tüm "iskelet" (HTML/CSS/JS) ve "görünüm" (Navbar, Footer), `_base.html` şablonu tarafından "miras" (inheritance) alınarak "profesyonelce" (senior) yönetilir.

### 2. "Profesyonel" (Senior) Backend (Django MVT + Formlar)
* **Modeller (MVT - Model):** `projects` ve `blog` modülleri, "kıdemli" (senior) veritabanı ilişkileri (örn: `ProjectGalleryImage` için `ForeignKey`) kullanır.
* **Zengin İçerik (CKEditor):** "Blog" modülü, "aptal" (dumb) `TextField` yerine, "profesyonel" (senior) bir "Zengin Metin Editörü" (`django-ckeditor`) kullanarak `/admin/` panelinden "grafik/resim/kod bloğu" yüklemeyi destekler.
* **Proje Galerisi (Inline Admin):** "Projeler" modülü, "kıdemli" (senior) bir "Bire-Çok" (One-to-Many) mimari kullanarak, `/admin/` panelinde "iç içe" (`TabularInline`) bir "Çoklu Resim Galerisi" yönetimi sunar.
* **Güvenli Formlar (MVT - Form):** "İletişim" modülü, `forms.py` kullanarak "profesyonel" (senior) `CSRF` korumalı ve "sunucu taraflı doğrulama" (server-side validation) yapan bir form kullanır.

### 3. "Kıdemli" (Senior) Güvenlik Mimarisi
* **Gizli Anahtar (Secret Key) Koruması:** `SECRET_KEY` ve `EMAIL_HOST_PASSWORD` gibi "hassas" (sensitive) veriler, `settings.py`'ye "hard-coded" (doğrudan) yazılmamış, `.env` dosyası kullanılarak "profesyonelce" (senior) soyutlanmıştır.
* **.gitignore:** `.env` dosyası ve `venv` klasörü, `.gitignore` tarafından "profesyonelce" (senior) görmezden gelinerek *asla* GitHub'a yüklenmez.
* **Spam Koruması (Ratelimit):** "İletişim" formu, "kıdemli" (senior) bir "profesyonel" (professional) kütüphane (`django-ratelimit`) kullanarak "Brute Force" ve "Spam" saldırılarına karşı (örn: 1 dakikada 5 istek) "profesyonelce" (senior) korunmaktadır.

### 4. "Profesyonel" (Professional) Frontend (Bootstrap 5 + Özel CSS)
* **Tasarım Mimarisi:** Site, `Bootstrap 5`'in "görünmez" (invisible) "Grid" (Izgara) ve "Yardımcı" (Utility) sınıflarını "temel" (base) olarak kullanır.
* **Özel Tema (CSS Variables):** "Jenerik" (generic) Bootstrap görünümünden kaçınmak için, `main.css` dosyası "kıdemli" (senior) "CSS Değişkenleri" (`:root`) kullanarak "profesyonel" (professional) ve "markalı" (branded) (Light Mode) bir "özel cilt" (custom skin) uygular.
* **Animasyonlar (AOS & CSS):** Sitede "durağan" (static) bir hissi engellemek için, `AOS (Animate on Scroll)` kütüphanesi (kaydırmada belirme) ve "profesyonel" (senior) CSS `transition`'ları (hover efektleri) kullanılır.

## 🚀 Kullanılan Ana Teknolojiler

* **Backend:** Django, Python
* **Frontend:** HTML5, CSS3 (CSS Variables), Bootstrap 5, AOS.js
* **Veritabanı:** SQLite (Geliştirme)
* **Admin/CMS:** django-ckeditor (Zengin Metin Editörü), Pillow (Resim İşleme)
* **Güvenlik:** django-ratelimit (Spam Koruması), django-environ (`.env` yönetimi)

## 🏃‍♂️ Yerel (Local) Kurulum

1.  Bu repoyu klonlayın.
2.  Bir sanal ortam (virtual environment) oluşturun: `python -m venv venv`
3.  Aktive edin: `.\venv\Scripts\activate` (Windows) veya `source venv/bin/activate` (macOS/Linux)
4.  Gerekli kütüphaneleri "profesyonelce" (senior) `requirements.txt`'den kurun: `pip install -r requirements.txt`
5.  Gerekli veritabanı "göçlerini" (migrations) uygulayın: `python manage.py migrate`
6.  Admin paneli için bir "süper kullanıcı" (superuser) oluşturun: `python manage.py createsuperuser`
7.  Sunucuyu başlatın: `python manage.py runserver`
8.  Siteye `http://127.0.0.1:8000/` adresinden, Admin paneline `http://127.0.0.1:8000/admin/` adresinden erişin.

## 👤 Yazar

* **EMRE AŞKIN**
* [(https://github.com/emreaskinsoftware)]
* [www.linkedin.com/in/emre-askin]