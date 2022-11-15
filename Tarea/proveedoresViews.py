from django.core import serializers
# Create your views here.
from django.shortcuts import render
from Tarea.models import Proveedor
from Tarea.forms import FilterProveedorFormulario, ProveedorFormulario


#Muestra todos los objetos
def proveedor(request):
    fromDB = Proveedor.objects.all()
    data = serializers.serialize("python", fromDB)

    context = {"data": data}
    return render(request, "Tarea/Proveedores/listaProveedores.html", context)


#Metodo POST
def proveedorPOST(request):
    if request.method == "POST":
        formulario = ProveedorFormulario(request.POST)
        
        if formulario.is_valid(): #Validación del formulario
            data = formulario.cleaned_data #Recuperación de datos
            proveedor = Proveedor( #Instanciación del objeto proveedor de la clase proveedor
                nombre = data["nombre"],
                rfc = data["rfc"],
                direccion = data["direccion"])
            proveedor.save() 

    else:
        formulario = ProveedorFormulario()

    context = {"formulario": formulario}
    return render(request, "Tarea/Proveedores/formularioProveedores.html", context)


#Metodo GET
def proveedorGET(request):
    data = {}
    if request.method == "GET":
        formulario = FilterProveedorFormulario(request.GET)

        if formulario.is_valid():
            finalForm = formulario.cleaned_data
            search = finalForm["nombre"] #Asignar a variable search el nombre
            
            fromDB = Proveedor.objects.all().filter(nombre = search)
            data = serializers.serialize("python", fromDB)

    else:
        data = FilterProveedorFormulario()

    context = {"data": data, "formulario": formulario}
    return render(request, "Tarea/Proveedores/filterProveedores.html", context) 

