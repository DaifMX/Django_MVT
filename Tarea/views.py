from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core import serializers
from Tarea.models import familiares

def familiar(request):
    mi_familia = familiares.objects.all()
    data = serializers.serialize("python", mi_familia)
    toRender = {
        "data": data
    }
    
    return render(request, "Tarea/index.html", toRender)