from django.contrib import admin

from .models import Categoria, Producto

admin.site.register(Categoria)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre')
admin.site.register(Producto, ProductAdmin)