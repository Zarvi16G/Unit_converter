from pint import UnitRegistry

from . import kelvin_to, fahrenheit_to, celsius_to

ureg = UnitRegistry()

def type_unit_form_temp(temperature, unit_from, unit_to):
    if unit_from == 'celsius':
        return temperature_celsius_to(temperature, unit_to)
    elif unit_from == 'fahrenheit':
        return temperature_fahrenheit_to(temperature, unit_to)
    elif unit_from == 'kelvin':
        return temperature_kelvin_to(temperature, unit_to)

def temperature_celsius_to(temperature, unit_to):
    if unit_to == 'fahrenheit':
        return celsius_to.temperature_celsius_to_fahrenheit(temperature)
    elif unit_to == 'kelvin':
        return celsius_to.temperature_celsius_to_kelvin(temperature)
    else:
        return celsius_to.temperature_celsius_to_celsius(temperature)

def temperature_fahrenheit_to(temperature, unit_to):
    if unit_to == 'celsius':
        return fahrenheit_to.temperature_fahrenheit_to_celsius(temperature)
    elif unit_to == 'kelvin':
        return fahrenheit_to.temperature_fahrenheit_to_kelvin(temperature)
    else:
        return fahrenheit_to.temperature_fahrenheit_to_fahrenheit(temperature)

def temperature_kelvin_to(temperature, unit_to):
    if unit_to == 'celsius':
        return kelvin_to.temperature_kelvin_to_celsius(temperature)
    elif unit_to == 'fahrenheit':
        return kelvin_to.temperature_kelvin_to_fahrenheit(temperature)
    else:
        return kelvin_to.temperature_kelvin_to_kelvin(temperature)
