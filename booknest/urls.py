from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'booknest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^booksys/', include('booksys.urls', namespace='booksys')),
    url(r'^admin/', include(admin.site.urls)),
)
