from django.conf.urls.defaults import include, patterns

# special urls for flatpage test cases
urlpatterns = patterns('',
    (r'^flatpage_root', include('django.contrib.flatpages.urls')),
    (r'^accounts/', include('django.contrib.auth.urls')),
)

