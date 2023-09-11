from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'titulo' : "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo' : "Respuesta",
        'nombre' : request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'nacionalidad' : request.POST['nacionalidad'],
        'idiomas' : request.POST.getlist('idiomas'),
        'correo' : request.POST['email'],
        'website' : request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)


# Formulario de operaciones basicas
def calculo(request):
    return render(request, 'encuesta/calculo.html')

def calculo_resultado(request):
    # Aquí realizarás la operación y mostrar resultado
    num1 = float(request.POST['num1'])
    num2 = float(request.POST['num2'])
    operacion = request.POST['operacion']

    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    else:
        resultado = None

    context = {
        'num1': num1,
        'num2': num2,
        'operacion': operacion,
        'resultado': resultado,
    }
    return render(request, 'encuesta/calculo_resultado.html', context)


# Formulario del volumen de un ciclindro
def cilindro(request):
    return render(request, 'encuesta/cilindro.html')

def cilindro_resultado(request):
    # Aquí realizará el cálculo del volumen
    altura = float(request.POST['altura'])
    diametro = float(request.POST['diametro'])

    # Calcula el radio a partir del diámetro
    radio = diametro / 2

    # Calcula el volumen del cilindro
    volumen = 3.14159265358979323846 * (radio ** 2) * altura

    context = {
        'altura': altura,
        'diametro': diametro,
        'volumen': volumen,
    }
    return render(request, 'encuesta/cilindro_resultado.html', context)
