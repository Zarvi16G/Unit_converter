from pint import UnitRegistry

# Inicializa el registro de unidades
ureg = UnitRegistry()

def length_foot_to_mm(length):
    """Convierte de pies a milímetros."""
    length_in_feet = length * ureg.foot
    length_in_millimeters = length_in_feet.to(ureg.millimeter)
    return length_in_millimeters.magnitude

def length_foot_to_cm(length):
    """Convierte de pies a centímetros."""
    length_in_feet = length * ureg.foot
    length_in_centimeters = length_in_feet.to(ureg.centimeter)
    return length_in_centimeters.magnitude

def length_foot_to_m(length):
    """Convierte de pies a metros."""
    length_in_feet = length * ureg.foot
    length_in_meters = length_in_feet.to(ureg.meter)
    return length_in_meters.magnitude

def length_foot_to_km(length):
    """Convierte de pies a kilómetros."""
    length_in_feet = length * ureg.foot
    length_in_kilometers = length_in_feet.to(ureg.kilometer)
    return length_in_kilometers.magnitude

def length_foot_to_yd(length):
    """Convierte de pies a yardas."""
    length_in_feet = length * ureg.foot
    length_in_yards = length_in_feet.to(ureg.yard)
    return length_in_yards.magnitude

def length_foot_to_inch(length):
    """Convierte de pies a pulgadas."""
    length_in_feet = length * ureg.foot
    length_in_inches = length_in_feet.to(ureg.inch)
    return length_in_inches.magnitude

def length_foot_to_mile(length):
    """Convierte de pies a millas."""
    length_in_feet = length * ureg.foot
    length_in_miles = length_in_feet.to(ureg.mile)
    return length_in_miles.magnitude
