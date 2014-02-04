from django.shortcuts import render
from portfolio.models import Page, Artwork

def index(request):
    page = Page.objects.all().filter(page_id='home')
    artwork = Artwork.objects.all()
    context = {'page': page, 'artwork': artwork}
    return render(request, 'index.html', context)