from pint import UnitRegistry

# Inicializa el registro de unidades
ureg = UnitRegistry()

def length_mm_to_mm(length):
    """Convierte de milímetros a milímetros (sin cambio)."""
    length_in_millimeters = length * ureg.millimeter
    return length_in_millimeters.magnitude  # Devolver el mismo valor

def length_mm_to_cm(length):
    """Convierte de milímetros a centímetros."""
    length_in_millimeters = length * ureg.millimeter
    length_in_centimeters = length_in_millimeters.to(ureg.centimeter)
    return length_in_centimeters.magnitude

def length_mm_to_m(length):
    """Convierte de milímetros a metros."""
    length_in_millimeters = length * ureg.millimeter
    length_in_meters = length_in_millimeters.to(ureg.meter)
    return length_in_meters.magnitude

def length_mm_to_km(length):
    """Convierte de milímetros a kilómetros."""
    length_in_millimeters = length * ureg.millimeter
    length_in_kilometers = length_in_millimeters.to(ureg.kilometer)
    return length_in_kilometers.magnitude

def length_mm_to_inch(length):
    """Convierte de milímetros a pulgadas."""
    length_in_millimeters = length * ureg.millimeter
    length_in_inches = length_in_millimeters.to(ureg.inch)
    return length_in_inches.magnitude

def length_mm_to_foot(length):
    """Convierte de milímetros a pies."""
    length_in_millimeters = length * ureg.millimeter
    length_in_feet = length_in_millimeters.to(ureg.foot)
    return length_in_feet.magnitude

def length_mm_to_yard(length):
    """Convierte de milímetros a yardas."""
    length_in_millimeters = length * ureg.millimeter
    length_in_yards = length_in_millimeters.to(ureg.yard)
    return length_in_yards.magnitude

def length_mm_to_mile(length):
    """Convierte de milímetros a millas."""
    length_in_millimeters = length * ureg.millimeter
    length_in_miles = length_in_millimeters.to(ureg.mile)
    return length_in_miles.magnitude
