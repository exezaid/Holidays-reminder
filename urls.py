from django.conf.urls.defaults import *
from django.conf import settings
from myregistration.forms import MyRegistrationForm
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^accounts/profile/', include('sitio.feriados.urls')),
    (r'^$', direct_to_template,{'template':'inicio.html'}, 'default'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #(r'^registro/', include('sitio.reg.urls')),
    #(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/register/$','registration.views.register', {
        'form_class': MyRegistrationForm}, 'registration_register'),
    (r'^accounts/', include('registration.urls')),
	(r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

