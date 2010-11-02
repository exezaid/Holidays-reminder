from django.db import models
from registration.models import RegistrationProfile

class MyRegistrationProfile(RegistrationProfile):
    pais = models.CharField(max_length=200, blank=True)
    provincia = models.CharField(max_length=200, blank=True)

