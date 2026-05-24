from django.shortcuts import render
from datetime import date
from .models import Work
# Create your views here.

def about(request):
    works = Work.objects.all()

    # --- Agrego script para la edad ---
    fecha_nacimiento = date(1984, 3, 4)
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    # ------------------------------

    # Paso AMBAS cosas al template: 'works' y 'edad'
    return render(request, "cv/about.html", {'works': works, 'edad': edad})

def cv(request):
    works = Work.objects.all()

    return render(request, "cv/cv.html", {'works':works})

def tech(request):

    return render(request, "cv/tech.html")