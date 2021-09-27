from django.contrib import admin

# Register your models here.
from .models import Categoria, Product

admin.site.register(Categoria)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'nombre')
admin.site.register(Product, ProductAdmin)