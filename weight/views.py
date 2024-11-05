from django.shortcuts import render
from . import conversions_weight

# Create your views here.
def index(request):
    return render(request, "weight_view.html")

def convert_weight(request):
    result = None
    if request.method == 'POST':
        # Obtén los datos del formulario
        weight = float(request.POST.get('weight'))  # Cambié length a temperature
        unit_from = request.POST.get('unit_from')
        unit_to = request.POST.get('unit_to')

        # Realiza la conversión
        result = conversions_weight.type_unit_form_weight(weight, unit_from, unit_to) 

    return render(request, 'weight/convert_weight.html', {'result': result, 'weight': weight, 'unit_from': unit_from, 'unit_to': unit_to})