from django.conf.urls.defaults import patterns

import views


urlpatterns = patterns('',
    (r'^request_attrs/$', views.request_processor),
)
