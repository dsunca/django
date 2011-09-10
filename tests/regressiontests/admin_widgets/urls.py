
from django.conf.urls.defaults import include, patterns 
import widgetadmin

urlpatterns = patterns('',
    (r'^', include(widgetadmin.site.urls)),
)
