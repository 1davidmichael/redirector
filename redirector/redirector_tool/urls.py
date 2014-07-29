from django.conf.urls import patterns, url

from redirector_tool import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<redirect_id>\d+)/$', views.detail, name='detail'),
)
