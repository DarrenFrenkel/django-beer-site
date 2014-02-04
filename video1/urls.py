from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'video1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	(r'^$', TemplateView.as_view(template_name='index.html')),
	(r'^beers/$', 'beer.views.BeersAll' ),
	(r'^beers/(?P<beerslug>.*)/$', 'beer.views.SpecificBeer')
	
)

urlpatterns += patterns('',
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),	   
)