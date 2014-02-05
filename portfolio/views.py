from django.shortcuts import render
from portfolio.models import Block, Artwork, Tag

def index(request):
    blocks = Block.objects.all()
    artworks = Artwork.objects.all()
    tags = Tag.objects.all()
    context = {'block_list': blocks, 'artwork_list': artworks}
    return render(request, 'index.html', context)