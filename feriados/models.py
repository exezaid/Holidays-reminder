from django.db import models

class Feriados(models.Model):
    feriado = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    dia = models.DateField('feriado el')

    def __unicode__(self):
        return self.feriado

    class Meta:
        verbose_name = u'feriado'
        verbose_name_plural = u'feriados' 

