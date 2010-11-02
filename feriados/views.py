from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Feriados
from django.contrib.auth.decorators import login_required

@login_required
def ver(request):
    feriado = Feriados.objects.all().order_by('dia')
    return render_to_response("feriados.html", dict(feriado=feriado))
