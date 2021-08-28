from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'titulo' : "Calculadora"
    }
    return render(request, 'calculo/basic.html', context)

def enviar(request):
    oper = request.POST['operacion']
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    rpta = 0
    if oper == 'suma':
        rpta = num1 + num2
    elif oper == 'resta':
        rpta = num1 - num2
    elif oper == 'multi':
        rpta = num1 * num2
    elif oper == 'divi':
        rpta = num1 / num2
    
    context = {
        'titulo' : "Resultado",
        'num1' : num1,
        'num2' : num2,
        'resultado' : '{:.2f}'.format(rpta),
        'operacion' : oper,
    }
    return render(request, 'calculo/resultado.html', context)
    