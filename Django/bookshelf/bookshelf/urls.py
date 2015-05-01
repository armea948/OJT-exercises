from django.conf.urls import patterns, include, url

from django.contrib import admin
from .views import authors_list
admin.autodiscover()
#from .views import
urlpatterns = patterns('bookshelf.views',
    # Examples:
    # url(r'^$', 'bookshelf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^authors/$', authors_list),
    #url(r'^time/$', current_datetime),
)
