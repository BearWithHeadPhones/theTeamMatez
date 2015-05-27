from django.conf.urls import patterns, include, url
from . import views


urlpatterns = patterns('',
    url(r'^update$', views.updateRanking),
    url(r'^updateLeaderBoard', views.updateLeaderBoard),
    url(r'^statistics/ranking/', views.ranking),

)
