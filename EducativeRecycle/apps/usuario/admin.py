from django.contrib import admin

# Register your models here.
from apps.usuario.models import Administrador,Juego,Jugador

admin.site.register(Administrador)
admin.site.register(Juego)
admin.site.register(Jugador)