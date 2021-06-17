from django.contrib import admin
from .models import *


# Register your models here.

class usuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "correo", "telefono", "rut", "direccion")


admin.site.register(usuario, usuarioAdmin)
