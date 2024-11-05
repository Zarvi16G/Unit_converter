from pint import UnitRegistry

ureg = UnitRegistry()

def temperature_kelvin_to_celsius(temperature):
    temperature_in_kelvin = ureg.Quantity(temperature, ureg.degK)
    temperature_in_celsius = temperature_in_kelvin.to(ureg.degC)
    return temperature_in_celsius.magnitude 

def temperature_kelvin_to_fahrenheit(temperature):
    temperature_in_kelvin = ureg.Quantity(temperature, ureg.degK)
    temperature_in_fahrenheit = temperature_in_kelvin.to(ureg.degF)
    return temperature_in_fahrenheit.magnitude 

def temperature_kelvin_to_kelvin(temperature):
    temperature_in_kelvin = ureg.Quantity(temperature, ureg.degK)
    return temperature_in_kelvin.magnitude

