from pint import UnitRegistry

# Inicializa el registro de unidades
ureg = UnitRegistry()

def length_yd_to_mm(length):
    """Convierte de yardas a milímetros."""
    length_in_yards = length * ureg.yard
    length_in_millimeters = length_in_yards.to(ureg.millimeter)
    return length_in_millimeters.magnitude

def length_yd_to_cm(length):
    """Convierte de yardas a centímetros."""
    length_in_yards = length * ureg.yard
    length_in_centimeters = length_in_yards.to(ureg.centimeter)
    return length_in_centimeters.magnitude

def length_yd_to_m(length):
    """Convierte de yardas a metros."""
    length_in_yards = length * ureg.yard
    length_in_meters = length_in_yards.to(ureg.meter)
    return length_in_meters.magnitude

def length_yd_to_km(length):
    """Convierte de yardas a kilómetros."""
    length_in_yards = length * ureg.yard
    length_in_kilometers = length_in_yards.to(ureg.kilometer)
    return length_in_kilometers.magnitude

def length_yd_to_inch(length):
    """Convierte de yardas a pulgadas."""
    length_in_yards = length * ureg.yard
    length_in_inches = length_in_yards.to(ureg.inch)
    return length_in_inches.magnitude

def length_yd_to_foot(length):
    """Convierte de yardas a pies."""
    length_in_yards = length * ureg.yard
    length_in_feet = length_in_yards.to(ureg.foot)
    return length_in_feet.magnitude

def length_yd_to_mile(length):
    """Convierte de yardas a millas."""
    length_in_yards = length * ureg.yard
    length_in_miles = length_in_yards.to(ureg.mile)
    return length_in_miles.magnitude
