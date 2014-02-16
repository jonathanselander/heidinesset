from django.shortcuts import render
from portfolio.models import Block, Artwork, Tag

def index(request):
    contact_block = Block.objects.get(block_id='contact')
    about_block = Block.objects.get(block_id='about')
    artworks = Artwork.objects.all()
    tags = Tag.objects.all()
    context = {
        'contact_block': contact_block,
        'about_block': about_block,
        'artwork_list': artworks
    }
    return render(request, 'index.html', context)