from django.conf.urls import patterns, include, url
from votez import views


urlpatterns = patterns('',

    url(r'^$', views.votingView),
    url(r'^vote/', views.vote),
)