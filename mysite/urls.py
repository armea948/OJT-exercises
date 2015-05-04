from django.conf.urls import patterns, include, url

from django.contrib import admin
#from views import hello
from polls.models import Poll
admin.autodiscover()
from .views import current_datetime , hours_ahead

urlpatterns = patterns('mysite.views',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', 'hello'),
    url(r'^$', 'hello'),
    url(r'^polls/$', include("polls.urls")),
    url(r'^hello/(?P<num>\d{1,2})$','hello'),    # \d{2} means it accept two digits
    url(r'^admin/polls/poll/$', Poll),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
