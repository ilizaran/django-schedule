from django.conf import settings
<<<<<<< HEAD
from django.views.generic import TemplateView
from django.conf.urls.defaults import patterns, url, include
from schedule import urls
=======
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

>>>>>>> 133f476f94afcb912beb2feefcfd41dc09a3d9e3
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),
    (r'^schedule/', include('schedule.urls')),

#    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
=======
    url(r'^$', direct_to_template,{"template":"homepage.html"}),
    (r'^schedule/', include('schedule.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
>>>>>>> 133f476f94afcb912beb2feefcfd41dc09a3d9e3
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

<<<<<<< HEAD

    
=======
>>>>>>> 133f476f94afcb912beb2feefcfd41dc09a3d9e3
