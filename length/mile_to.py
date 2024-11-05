from pint import UnitRegistry

# Inicializa el registro de unidades
ureg = UnitRegistry()

def length_mile_to_mm(length):
    """Convierte de millas a milímetros."""
    length_in_miles = length * ureg.mile
    length_in_millimeters = length_in_miles.to(ureg.millimeter)
    return length_in_millimeters.magnitude

def length_mile_to_cm(length):
    """Convierte de millas a centímetros."""
    length_in_miles = length * ureg.mile
    length_in_centimeters = length_in_miles.to(ureg.centimeter)
    return length_in_centimeters.magnitude

def length_mile_to_m(length):
    """Convierte de millas a metros."""
    length_in_miles = length * ureg.mile
    length_in_meters = length_in_miles.to(ureg.meter)
    return length_in_meters.magnitude

def length_mile_to_km(length):
    """Convierte de millas a kilómetros."""
    length_in_miles = length * ureg.mile
    length_in_kilometers = length_in_miles.to(ureg.kilometer)
    return length_in_kilometers.magnitude

def length_mile_to_yd(length):
    """Convierte de millas a yardas."""
    length_in_miles = length * ureg.mile
    length_in_yards = length_in_miles.to(ureg.yard)
    return length_in_yards.magnitude

def length_mile_to_inch(length):
    """Convierte de millas a pulgadas."""
    length_in_miles = length * ureg.mile
    length_in_inches = length_in_miles.to(ureg.inch)
    return length_in_inches.magnitude

def length_mile_to_foot(length):
    """Convierte de millas a pies."""
    length_in_miles = length * ureg.mile
    length_in_feet = length_in_miles.to(ureg.foot)
    return length_in_feet.magnitude
