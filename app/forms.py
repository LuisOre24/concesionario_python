from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Marca, Tipo, Transmision,Auto


class LoginForm(AuthenticationForm):
    def __init__(self, request: None, *args ,**kwargs) -> None:
        super().__init__(request=request, *args, **kwargs)

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        labels = {
            'marca' : 'Marca'
        }
        widgets = {
            'marca' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese la Marca del Vehiculo'
                }
            )
        }

class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'
        labels = {
            'tipo' : 'Tipo'
        }
        widgets = {
            'tipo' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese la Marca del Vehiculo'
                }
            )
        }

class TransmisionForm(forms.ModelForm):
    class Meta:
        model = Transmision
        fields = '__all__'
        labels = {
            'transmision' : 'Transmision'
        }
        widgets = {
            'transmision' : forms.TextInput(
                attrs={
                    'placeholder': 'Tipo de Transmision'
                }
            )
        }

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
        labels = {
            'modelo' : 'Modelo',
            'id_Marca' : 'Marca',
            'version' : 'Version',
            'id_Tipo' : 'Tipo',
            'costo' : 'Precio',
            'motor' : 'Motor',
            'potencia' : 'Potencia',
            'torque' : 'Torque',
            'cilindrada' : 'Cilindrada',
            'id_transmision' : 'Transmision',
            'año_fabricacion' : 'Año',
            'largo' : 'Largo',
            'ancho' : 'Ancho',
            'alto' : 'Alto',
            'estado' : 'Estado',
            'imagen' : 'Imagen'
        }
        widgets = {
            'modelo' : forms.TextInput(),
            'id_Marca' : forms.SelectMultiple(),
            'version' : forms.TextInput(),
            'id_Tipo' : forms.SelectMultiple(),
            'costo' : forms.TextInput(),
            'motor' : forms.TextInput(),
            'potencia' : forms.TextInput(),
            'torque' : forms.TextInput(),
            'cilindrada' : forms.TextInput(),
            'id_transmision' : forms.SelectMultiple(),
            'año_fabricacion' : forms.TextInput(),
            'largo' : forms.TextInput(),
            'ancho' : forms.TextInput(),
            'alto' : forms.TextInput(),
            'estado' : forms.TextInput(),
            'imagen' : forms.ImageField()
        }