from django.conf.urls.defaults import include, patterns
from django.contrib import admin

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)
