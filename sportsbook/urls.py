from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sportsbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^management/', include('management.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'management.views.login_page', name="login_page"),
    url(r'^logout/', 'management.views.logout_page', name="logout_page"),
    url(r'^$', RedirectView.as_view(url= '/login/'))
)
