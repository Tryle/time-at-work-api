from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'timeatworkapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('quickstart.urls')),
)
