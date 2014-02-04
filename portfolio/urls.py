from django.conf.urls import patterns, include, url
#from django.conf.urls.static import static
#from django.conf import settings

from portfolio import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
