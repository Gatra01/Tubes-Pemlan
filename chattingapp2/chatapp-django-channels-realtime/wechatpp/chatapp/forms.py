# Buat file forms.py di direktori aplikasi Anda

from django import forms

class PersonalChatForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
