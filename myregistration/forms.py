from django import forms
from registration.forms import RegistrationForm
from django.contrib.auth.models import Permission

p=Permission.objects.get(name="Can add feriados")
d=Permission.objects.get(name="Can delete feriados")
c=Permission.objects.get(name="Can change feriados")

class MyRegistrationForm(RegistrationForm):
    pais = forms.CharField(max_length=200)
    provincia = forms.CharField(max_length=200)

    def save(self, profile_callback=None):
        new_user = super(MyRegistrationForm, self).save(profile_callback)
        new_user.provincia = self.cleaned_data['provincia']
        new_user.pais = self.cleaned_data['pais']
        new_user.is_staff = True
        new_user.user_permissions.add(p,d,c)
        new_user.save()
        return new_user

