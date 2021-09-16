from django.contrib import admin

# Register your models here.
from .models import Categoria, Product, Cliente

admin.site.register(Categoria)
admin.site.register(Product)
admin.site.register(Cliente)