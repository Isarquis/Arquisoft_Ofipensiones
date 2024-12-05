from django.shortcuts import render
from django.http import HttpResponse
from ofipensiones.auth0backend import getRole
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .logic import logic_estudiante as le



@csrf_exempt
def estudiantes_estudiante_view(request, cod):
    role=getRole(request)
    if role=="Estudiante":
        if request.method=='GET':
            
            estudiantes=le.get_estudiantes(cod)
            if estudiantes[0].estudiante.correo==request.user.email:
                return HttpResponse(estudiantes, 'application/json')
            else:
                return HttpResponse("No tiene acceso")
    else:
        return HttpResponse("No tiene acceso")