# contact/forms.py
from django import forms

class ContactForm(forms.Form):
    """
    Kullanıcıdan 'güvenli' bir şekilde veri almak için 
    Django'nun 'forms' altyapısını kullanıyoruz.
    """
    # forms.CharField -> <input type="text">
    name = forms.CharField(
        max_length=100,
        label="İsminiz",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsminizi girin'})
    )

    # forms.EmailField -> Email doğrulaması yapar
    email = forms.EmailField(
        label="E-posta Adresiniz",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'isminiz@example.com'})
    )

    # forms.CharField + forms.Textarea -> <textarea>
    message = forms.CharField(
        label="Mesajınız",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Mesajınızı buraya yazın...'})
    )

    # 'widget=forms.TextInput' kısımları, Bootstrap CSS'imizle
    # (form-control) uyumlu, "profesyonel" ve "tasarımlı"
    # form alanları oluşturmak içindir.