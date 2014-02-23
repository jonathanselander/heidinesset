# -*- coding: utf-8 -*-

from django.shortcuts import render
from portfolio.models import Block, Artwork, Tag
from portfolio.forms import ContactForm
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            validation = request.POST['validation'].strip().lower()
            if validation == 'nesset' or validation == 'heidi nesset' or validation == 'heidi' or validation == 'heidinesset':
                message = u'Ämne: ' + request.POST['subject'] + "\n" \
                    u'Avsändare: ' + request.POST['sender'] + "\n\n" \
                    'Meddelande:' + "\n" + request.POST['message']

                send_mail(u'Kontaktförfrågan från heidinesset.com', message, 'web@heidinesset.com',
                    ['heidi@heidinesset.com'], fail_silently=False)


    try:
        contact_block = Block.objects.get(block_id='contact')
    except:
        contact_block = None

    try:
        about_block = Block.objects.get(block_id='about')
    except:
        about_block = None

    try:
        footer_block = Block.objects.get(block_id='footer')
    except:
        footer_block = None

    artworks = Artwork.objects.all()
    contact_form = ContactForm()
    tags = Tag.objects.all()
    context = {
        'contact_block': contact_block,
        'contact_form': contact_form,
        'footer_block': footer_block,
        'about_block': about_block,
        'artwork_list': artworks,
        'tag_list': tags
    }
    return render(request, 'index.html', context)
