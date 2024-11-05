from pint import UnitRegistry

ureg = UnitRegistry()

def temperature_celsius_to_fahrenheit(temperature):
    temperature_in_celsius = ureg.Quantity(temperature, ureg.degC)
    temperature_in_fahrenheit = temperature_in_celsius.to(ureg.degF)
    return temperature_in_fahrenheit.magnitude

def temperature_celsius_to_kelvin(temperature):
    temperature_in_celsius = ureg.Quantity(temperature, ureg.degC)
    temperature_in_kelvin = temperature_in_celsius.to(ureg.K)
    return temperature_in_kelvin.magnitude

def temperature_celsius_to_celsius(temperature):
    temperature_in_celsius = ureg.Quantity(temperature, ureg.degC)
    return temperature_in_celsius.magnitude
