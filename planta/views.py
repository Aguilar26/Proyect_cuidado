from django.shortcuts import render, redirect
from .models import Plant

def sugerencia_form(request):
    if request.method == 'POST':
        # Capturar condiciones del usuario
        water = request.POST.get('water')
        light = request.POST.get('light')
        location = request.POST.get('location')
        maintenance = request.POST.get('maintenance')

        # Filtrar plantas que cumplan esas condiciones
        sugeridas = Plant.objects.filter(
            water=water,
            light=light,
            location=location,
            maintenance=maintenance
        )

        # Renderizar resultados
        return render(request, 'planta/sugerencia_resultados.html', {'plants': sugeridas})

    return render(request, 'planta/sugerencia_form.html')


def sugerencia_resultados(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'planta/sugerencia_resultados.html', {'plant': plant})
