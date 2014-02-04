from django.shortcuts import render
from portfolio.models import Page, Artwork, Tag

def index(request):
    page = Page.objects.all().filter(page_id='home').first()
    artworks = Artwork.objects.all()
    tags = Tag.objects.all()
    context = {'page': page, 'artwork_list': artworks}
    return render(request, 'index.html', context)