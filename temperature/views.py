from django.shortcuts import render
from . import conversions_temp

# Create your views here.
def index(request):
    return render(request, "temperature_view.html")

def convert_temperature(request):
    result = None
    if request.method == 'POST':
        # Obtén los datos del formulario
        temperature = float(request.POST.get('temperature'))  # Cambié length a temperature
        unit_from = request.POST.get('unit_from')
        unit_to = request.POST.get('unit_to')

        # Realiza la conversión
        result = conversions_temp.type_unit_form_temp(temperature, unit_from, unit_to) 

    return render(request, 'temperature/convert_temperature.html', {'result': result, 'temperature': temperature, 'unit_from': unit_from, 'unit_to': unit_to})  # Cambié length a temperature

