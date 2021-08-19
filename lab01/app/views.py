from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Respuesta Desde la vista de APP!")

def suma(request, num1, num2):
    sum = num1 + num2
    return HttpResponse("La suma de %s + %s = %s" % (num1, num2, sum))

def resta(request, num1, num2):
    res = num1 - num2
    return HttpResponse("La resta de %s - %s = %s" % (num1, num2, res))

def multiplicacion(request, num1, num2):
    mult = num1 * num2
    return HttpResponse("La multiplicacion de %s x %s = %s" % (num1, num2, mult))

def division(request, num1, num2):
    div = num1 / num2
    return HttpResponse("La multiplicacion de %s / %s = %.3f" % (num1, num2, div))
