from pint import UnitRegistry

# Inicializa el registro de unidades
ureg = UnitRegistry()

def length_inch_to_mm(length):
    """Convierte de pulgadas a milímetros."""
    length_in_inches = length * ureg.inch
    length_in_millimeters = length_in_inches.to(ureg.millimeter)
    return length_in_millimeters.magnitude

def length_inch_to_cm(length):
    """Convierte de pulgadas a centímetros."""
    length_in_inches = length * ureg.inch
    length_in_centimeters = length_in_inches.to(ureg.centimeter)
    return length_in_centimeters.magnitude

def length_inch_to_m(length):
    """Convierte de pulgadas a metros."""
    length_in_inches = length * ureg.inch
    length_in_meters = length_in_inches.to(ureg.meter)
    return length_in_meters.magnitude

def length_inch_to_km(length):
    """Convierte de pulgadas a kilómetros."""
    length_in_inches = length * ureg.inch
    length_in_kilometers = length_in_inches.to(ureg.kilometer)
    return length_in_kilometers.magnitude

def length_inch_to_yd(length):
    """Convierte de pulgadas a yardas."""
    length_in_inches = length * ureg.inch
    length_in_yards = length_in_inches.to(ureg.yard)
    return length_in_yards.magnitude

def length_inch_to_foot(length):
    """Convierte de pulgadas a pies."""
    length_in_inches = length * ureg.inch
    length_in_feet = length_in_inches.to(ureg.foot)
    return length_in_feet.magnitude

def length_inch_to_mile(length):
    """Convierte de pulgadas a millas."""
    length_in_inches = length * ureg.inch
    length_in_miles = length_in_inches.to(ureg.mile)
    return length_in_miles.magnitude
