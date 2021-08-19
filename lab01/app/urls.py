from django.urls import path

from . import views

urlpatterns = [
    # ex: localhost:8080/app/
    path('', views.index, name='index'),
    # ex: localhost:8080/app/sumar/18/19
    path('sumar/<int:num1>/<int:num2>', views.suma, name='suma'),
    # ex: localhost:8080/app/restar/30/10
    path('restar/<int:num1>/<int:num2>', views.resta, name='resta'),
    # ex: localhost:8080/app/dividir/5/4
    path('multiplicar/<int:num1>/<int:num2>', views.multiplicacion, name='multiplicar'),
    # ex: localhost:8080/app/dividir/5/4
    path('dividir/<int:num1>/<int:num2>', views.division, name='dividir'),
]