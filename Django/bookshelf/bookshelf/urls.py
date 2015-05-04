from django.conf.urls import patterns, url#, include

from django.contrib import admin
from .views import authors_list, authors_detail, book_list, index_page
admin.autodiscover()
#from .views import
urlpatterns = patterns('bookshelf.views',
    # Examples:
    # url(r'^$', 'bookshelf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index_page),
    url(r'^authors/$', authors_list),
    url(r'^authors/(?P<num>\d{1,2})/$', authors_detail),
    url(r'^books/$', book_list)
    #url(r'^time/$', current_datetime),
)
