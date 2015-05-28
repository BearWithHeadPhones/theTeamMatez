from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static,settings

from django.contrib import admin
from settings import DEBUG
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theteammatez.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('votez.urls')),
    url(r'', include('statistics.urls')),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'auth/login.html'}),
    url(r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/'}),
)

urlpatterns += staticfiles_urlpatterns()
if(settings.DEBUG):

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
