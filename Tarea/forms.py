from django import forms

# +----------------------------+
# |          PERSONAS          |
# +----------------------------+
class PersonaFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    fecha_nacimiento = forms.DateField()

class FilterPersonaFormulario(forms.Form):
    apellido = forms.CharField()


# +----------------------------+
# |        PROVEEDORES         |
# +----------------------------+

class ProveedorFormulario(forms.Form):
    nombre = forms.CharField()
    rfc = forms.CharField()
    direccion = forms.CharField()

class FilterProveedorFormulario(forms.Form):
    nombre = forms.CharField()


# +----------------------------+
# |         PRODUCTOS          |
# +----------------------------+

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    sku = forms.CharField()
    stock = forms.IntegerField()

class FilterProductoFormulario(forms.Form):
    sku = forms.CharField()
