from django.db import models


# Modelo para los usuarios principales (representantes)
class UsuarioPrincipal(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    rango = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rango} - {self.username}"


# Modelo para los miembros nuevos
from django.core.validators import RegexValidator

class MiembroNuevo(models.Model):
    nombre_completo = models.CharField(max_length=200)
    celular = models.CharField(max_length=15, default="No especificado")

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo
