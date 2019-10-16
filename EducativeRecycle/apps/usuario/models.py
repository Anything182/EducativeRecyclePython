from django.db import models

# Create your models here.

class Jugador(models.Model):
    nombreJugador = models.CharField(max_length=20)
    generoJugador = models.CharField(max_length=1)
    edadJugador = models.IntegerField()
    correoJugador = models.EmailField()
    usuarioJugador=models.CharField(max_length=30)
    contraseñaJugador = models.CharField(max_length=30)
    

class Juego(models.Model):
    puntajeObtenido = models.IntegerField()
    puntajeTotal = models.IntegerField()
    jugador = models.ForeignKey(Jugador,null=True,on_delete=models.DO_NOTHING)



class Administrador(models.Model):
    nombreAdmin=models.CharField(max_length=50)
    correoRoot=models.EmailField()
    UsuarioRoot=models.CharField(max_length=30)
    contraseñaRoot=models.CharField(max_length=20)
    juego = models.ForeignKey(Jugador,null=True,on_delete=models.DO_NOTHING)
