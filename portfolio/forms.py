from django import forms
from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, initial='Ditt namn')
    sender = forms.EmailField(initial='din@epostadress.se')
    validation = forms.CharField(max_length=100, initial='Antispam: Fyll i mitt efternamn')
    message = forms.CharField(widget=forms.Textarea, initial='Meddelande')