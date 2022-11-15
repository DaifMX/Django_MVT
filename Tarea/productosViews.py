from django.core import serializers
# Create your views here.
from django.shortcuts import render
from Tarea.models import Producto
from Tarea.forms import FilterProductoFormulario, ProductoFormulario


#Muestra todos los objetos
def producto(request):
    fromDB = Producto.objects.all()
    data = serializers.serialize("python", fromDB)

    context = {"data": data}
    return render(request, "Tarea/Productos/listaProductos.html", context)


#Metodo POST
def productoPOST(request):
    if request.method == "POST":
        formulario = ProductoFormulario(request.POST)
        
        if formulario.is_valid(): #Validación del formulario
            data = formulario.cleaned_data #Recuperación de datos
            producto = Producto( #Instanciación del objeto producto de la clase producto
                nombre = data["nombre"],
                sku = data["sku"],
                stock = data["stock"])
            producto.save() 

    else:
        formulario = ProductoFormulario()

    context = {"formulario": formulario}
    return render(request, "Tarea/Productos/formularioProductos.html", context)


#Metodo GET
def productoGET(request):
    data = {}
    if request.method == "GET":
        formulario = FilterProductoFormulario(request.GET)

        if formulario.is_valid():
            finalForm = formulario.cleaned_data
            search = finalForm["sku"] #Asignar a variable search el sku
            
            fromDB = Producto.objects.all().filter(sku = search)
            data = serializers.serialize("python", fromDB)

    else:
        data = FilterProductoFormulario()

    context = {"data": data, "formulario": formulario}
    return render(request, "Tarea/Productos/filterProductos.html", context) 

