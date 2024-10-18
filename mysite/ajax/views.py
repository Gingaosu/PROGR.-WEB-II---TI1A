from django.shortcuts import render
from django.http import JsonResponse
from .models import Estado, Municipio

def index(request):
    estados = Estado.objects.all().order_by('nombre')
    return render(request, 'ajax/index.html', {'estados': estados})

def cargar_municipios(request):
    estado_id = request.GET.get('estado_id')
    municipios = Municipio.objects.filter(estado_id=estado_id).order_by('nombre')
    return JsonResponse(list(municipios.values('id', 'nombre')), safe=False)
