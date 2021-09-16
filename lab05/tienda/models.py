from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Fecha Creación')

    def __str__(self):
        return self.nombre

class Product(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField("Fecha de Nacimiento")
    pub_date = models.DateTimeField('Fecha Creación')
    def __str__(self):
        return self.nombre+ " " + self.apellido