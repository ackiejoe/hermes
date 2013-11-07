from django.conf.urls import patterns, url

from flyer import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)