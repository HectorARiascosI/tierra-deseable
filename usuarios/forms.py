from django import forms
from .models import MiembroNuevo


class usuarioPrincipalLoginForm(forms.Form):
    username= forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'usuario'}))
    password= forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class': 'form', 'placeholder': 'password'}))
    
    
class MiembroNuevoForm(forms.ModelForm):
    class Meta:
        model = MiembroNuevo
        fields = ['nombre_completo', 'celular']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Completo'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Celular de contacto'}),
        }

    