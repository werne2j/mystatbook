from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
from management.views import *
from sportsbook import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sportsbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^management/', include('management.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^register/', UserRegistration.as_view(), name='registration'),
    url(r'^login/', 'management.views.login_page', name="login_page"),
    url(r'^logout/', 'management.views.logout_page', name="logout_page"),
    url(r'^$', Front.as_view(), name='home'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
