from django.shortcuts import render
from portfolio.models import Block, Artwork, Tag
from portfolio.forms import ContactForm

def index(request):
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