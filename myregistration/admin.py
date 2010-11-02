from django.contrib import admin
from registration.models import RegistrationProfile
from registration.admin import RegistrationAdmin
from myregistration.models import MyRegistrationProfile

try:
    admin.site.unregister(RegistrationProfile)
except admin.sites.NotRegistered:
    pass

admin.site.register(MyRegistrationProfile, RegistrationAdmin)

