from django.core import serializers
# Create your views here.
from django.shortcuts import render
from Tarea.models import Persona
from Tarea.forms import PersonaFormulario


#Muestra todos los objetos 
def persona(request):
    fromDB = Persona.objects.all()
    data = serializers.serialize("python", fromDB)
    context = {
        "data": data
    }
    
    return render(request, "Tarea/listaPersonas.html", context)


def updateDB(request):
    if request.method == "POST": #Si el request es de metodo POST...
        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid(): #Validación del formulario
            data = formulario.cleaned_data #Recuperación de datos
            persona = Persona( #Instanciación del objeto persona de la clase persona
                nombre=data["nombre"],
                apellido=data["apellido"],
                telefono=data["telefono"],
                fecha_nacimiento=data["fecha_nacimiento"])
                
            persona.save() 

    else:
        formulario = PersonaFormulario()

    context = {"formulario": formulario}
    return render(request, "Tarea/formularioPersonas.html", context)


def searchDB(request):
    fromDB = Persona.objects.filter(id = 1).values()
    data = serializers.serialize("python", fromDB)

    return render(request, "Tarea/filterPersonas.html", data)

