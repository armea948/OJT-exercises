from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    #url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
    url(r'^sign_up/$', views.signUp),
    url(r'^author/$', views.addAuthor),
    url(r'^publisher/$', views.addPublisher),
    url(r'^book/$', views.addBook),
    url(r'^login/$', views.my_view),
    url(r'^home/$', views.home),
    url(r'^logout/$', views.logout_view),
)
