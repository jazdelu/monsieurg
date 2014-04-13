from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'monsieurg.views.homepage', name='homepage'),
    url(r'^index/', 'monsieurg.views.homepage', name='homepage'),
    # url(r'^blog/', include('blog.urls')),
    #(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^order/','theme.views.order', name ='order'),
    url(r'^review/$','product.views.latest', name = 'review latest'),
    url(r'^review/(?P<tid>.+)/$','product.views.review', name = 'review'),
    url(r'^story/','monsieurg.views.story', name = 'story'),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'monsieurg.views.raise404'

