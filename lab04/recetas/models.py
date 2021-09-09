from django.db import models
from django.db.models.base import Model

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField()

    def str(self):
        return self.nombre

class Receta(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.TextField()
    tiempo_registro = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def str(self):
        return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta,on_delete=models.CASCADE)
    texto = models.TextField(help_text=u'Tu comentario', verbose_name='Comentario')

    def str(self):
        return self.texto