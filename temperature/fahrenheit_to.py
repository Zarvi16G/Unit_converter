from pint import UnitRegistry

ureg = UnitRegistry()

def temperature_fahrenheit_to_celsius(temperature):
    temperature_in_fahrenheit = ureg.Quantity(temperature, ureg.degF)
    temperature_in_celsius = temperature_in_fahrenheit.to(ureg.degC)
    return temperature_in_celsius.magnitude 

def temperature_fahrenheit_to_kelvin(temperature):
    temperature_in_fahrenheit = ureg.Quantity(temperature, ureg.degF)
    temperature_in_kelvin = temperature_in_fahrenheit.to(ureg.degK)
    return temperature_in_kelvin.magnitude 

def temperature_fahrenheit_to_fahrenheit(temperature):
    temperature_in_fahrenheit = ureg.Quantity(temperature, ureg.degF)
    return temperature_in_fahrenheit.magnitude
