from django.http import HttpResponse
import datetime
from django.template.loader import get_template

class Persona(object):
    def __init__(self, Nombre, Apellido, Edad) -> None:
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad

def plantillasuperior(request):

    hoja = get_template("Plan_Super.html")
    
    return HttpResponse(hoja.render())

def Hola(request):
    docexterno = get_template("Plan_Super.html")
    
    return HttpResponse(docexterno.render())

def fechaactual(request):
    Temas = ["Tema1", "Tema2", "Tema3", "Tema4"]

    P1 = Persona("Nicolas", "Núñez", "26 años")

    docexterno1 = get_template("plantilla2.html")

    fact = datetime.datetime.now()
    
    dicc = {
            "Nombre": P1.Nombre,
            "Apellido": P1.Apellido,
            "Edad": P1.Edad,
            "Temas": Temas,
            "fechaactual": fact
            }
    
    return HttpResponse(docexterno1.render(dicc))