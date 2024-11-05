from django.shortcuts import render
from . import conversions

# Create your views here.
def index(request):
    return render(request, 'length_view.html')

def convert_length(request):
    result = None
    if request.method == 'POST':
        # Obtén los datos del formulario
        length = float(request.POST.get('length'))
        unit_from = request.POST.get('unit_from')
        unit_to = request.POST.get('unit_to')

        # Realiza la conversión
        result = conversions.type_unit_form(length, unit_from, unit_to)

    return render(request, 'length/convert_length.html', {'result': result, 'length': length, 'unit_from': unit_from, 'unit_to': unit_to})