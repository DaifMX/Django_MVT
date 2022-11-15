from django.core import serializers
# Create your views here.
from django.shortcuts import render
from Tarea.models import Persona
from Tarea.forms import FilterPersonaFormulario, PersonaFormulario


#Muestra todos los objetos 
def persona(request):
    fromDB = Persona.objects.all()
    data = serializers.serialize("python", fromDB)

    context = {"data": data}
    return render(request, "Tarea/Personas/listaPersonas.html", context)


#Metodo POST
def personaPOST(request):
    if request.method == "POST":
        formulario = PersonaFormulario(request.POST)
        
        if formulario.is_valid(): #Validación del formulario
            data = formulario.cleaned_data #Recuperación de datos
            persona = Persona( #Instanciación del objeto persona de la clase persona
                nombre = data["nombre"],
                apellido = data["apellido"],
                telefono = data["telefono"],
                fecha_nacimiento = data["fecha_nacimiento"])
            persona.save() 

    else:
        formulario = PersonaFormulario()

    context = {"formulario": formulario}
    return render(request, "Tarea/Personas/formularioPersonas.html", context)


#Metodo GET
def personaGET(request):
    data = {}
    if request.method == "GET":
        formulario = FilterPersonaFormulario(request.GET)

        if formulario.is_valid():
            finalForm = formulario.cleaned_data
            search = finalForm["apellido"]
            
            fromDB = Persona.objects.all().filter(apellido = search)
            data = serializers.serialize("python", fromDB)

    else:
        data = FilterPersonaFormulario()

    context = {"data": data, "formulario": formulario}
    return render(request, "Tarea/Personas/filterPersonas.html", context) 

