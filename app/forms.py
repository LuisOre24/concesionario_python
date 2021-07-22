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
                    'class': 'form-control',
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
                    'class': 'form-control',
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
                    'class': 'form-control',
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
            'modelo' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Modelo del Auto'
                }
            ),
            'id_Marca' : forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Marca'
                }
            ),
            'version' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Version'
                }
            ),
            'id_Tipo' : forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tipo de Transmision'
                }
            ),
            'costo' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Costo'
                }
            ),
            'motor' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Motor'
                }
            ),
            'potencia' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Potencia'
                }
            ),
            'torque' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Torque'
                }
            ),
            'cilindrada' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cilindrada'
                }
            ),
            'id_transmision' : forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Tipo de Transmision'
                }
            ),
            'año_fabricacion' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Año de Fabricacion'
                }
            ),
            'largo' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Largo del Vehivulo'
                }
            ),
            'ancho' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ancho del Vehiculo'
                }
            ),
            'alto' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Alto del vehiculo'
                }
            ),
            'estado' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estado'
                }
            ),
            'imagen' : forms.ImageField()

        }