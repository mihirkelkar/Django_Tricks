from django.conf.urls import patterns, include, url
from back_change.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'back_change.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'back_change.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
