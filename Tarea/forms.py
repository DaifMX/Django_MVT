from django import forms

class PersonaFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    telefono = forms.IntegerField()
    fecha_nacimiento = forms.DateField()

class FilterPersonaFormulario(forms.Form):
    id = forms.IntegerField()