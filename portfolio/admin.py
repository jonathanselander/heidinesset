from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget
from django.db import models

# Register your models here.
from portfolio.models import Artwork, Tag, Block

class PortfolioAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Artwork, PortfolioAdmin)
admin.site.register(Tag)
admin.site.register(Block, PortfolioAdmin)
