# contact/views.py (YENİDEN YAZILDI - v1.2 MİMARİSİ)

from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Message # <-- YENİ: Veritabanı modelimizi import et
from django.contrib import messages
from django.utils import timezone
import datetime

# "Kıdemli" (Senior) Spam Korumamız (Aşama 27'den - Bu hala gerekli!)
def check_spam_protection(request):
    last_submission_time_str = request.session.get('last_submission_time')
    if last_submission_time_str:
        try:
            last_submission_time = datetime.datetime.fromisoformat(last_submission_time_str)
            if timezone.is_naive(last_submission_time):
                last_submission_time = timezone.make_aware(last_submission_time, timezone.get_default_timezone())

            now = timezone.now()
            time_passed = now - last_submission_time

            if time_passed.total_seconds() < 60: # 60 saniye spam koruması
                return False # SPAM
        except ValueError:
            pass # Bozuk session verisi, devam et
    return True # Güvenli


# --- GÖRÜNÜM (VIEW) ---
def contact_view(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            # 1. SPAM KONTROLÜ (Hala çalışıyor)
            if not check_spam_protection(request):
                messages.error(request, 'Çok hızlı form göndermeye çalıştınız. Lütfen 1 dakika bekleyip tekrar deneyin.')
                return render(request, 'contact/contact_form.html', {'form': form}, status=429)


            # 2. VERİYİ AL
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_content = form.cleaned_data['message']

            # --- PROFESYONEL (SENIOR) DEĞİŞİKLİK (v1.2) ---
            # 'send_mail(...)' komutunu SİL.
            # Yerine, "kıdemli" (senior) bir şekilde veritabanına KAYDET.

            Message.objects.create(
                name=name,
                email=email,
                message=message_content
            )
            # -----------------------------------------------

            # 3. BAŞARI VE YÖNLENDİRME
            request.session['last_submission_time'] = timezone.now().isoformat()
            messages.success(request, 'Mesajınız başarıyla alındı! En kısa sürede inceleyeceğim.')
            return redirect('contact')

    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contact/contact_form.html', context)