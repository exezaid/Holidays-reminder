from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^$', 'reg.views.register'),
)
