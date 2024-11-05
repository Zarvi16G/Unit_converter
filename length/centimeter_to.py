from pint import UnitRegistry

# Inicializa el registro de unidades
ureg = UnitRegistry()

def length_cm_to_mm(length):
    """Convierte de centímetros a milímetros."""
    length_in_centimeters = length * ureg.centimeter
    length_in_millimeters = length_in_centimeters.to(ureg.millimeter)
    return length_in_millimeters.magnitude

def length_cm_to_cm(length):
    """Convierte de centímetros a centímetros (sin cambio)."""
    length_in_centimeters = length * ureg.centimeter
    return length_in_centimeters.magnitude  # Devolver el mismo valor

def length_cm_to_m(length):
    """Convierte de centímetros a metros."""
    length_in_centimeters = length * ureg.centimeter
    length_in_meters = length_in_centimeters.to(ureg.meter)
    return length_in_meters.magnitude

def length_cm_to_km(length):
    """Convierte de centímetros a kilómetros."""
    length_in_centimeters = length * ureg.centimeter
    length_in_kilometers = length_in_centimeters.to(ureg.kilometer)
    return length_in_kilometers.magnitude

def length_cm_to_inch(length):
    """Convierte de centímetros a pulgadas."""
    length_in_centimeters = length * ureg.centimeter
    length_in_inches = length_in_centimeters.to(ureg.inch)
    return length_in_inches.magnitude

def length_cm_to_foot(length):
    """Convierte de centímetros a pies."""
    length_in_centimeters = length * ureg.centimeter
    length_in_feet = length_in_centimeters.to(ureg.foot)
    return length_in_feet.magnitude

def length_cm_to_yard(length):
    """Convierte de centímetros a yardas."""
    length_in_centimeters = length * ureg.centimeter
    length_in_yards = length_in_centimeters.to(ureg.yard)
    return length_in_yards.magnitude

def length_cm_to_mile(length):
    """Convierte de centímetros a millas."""
    length_in_centimeters = length * ureg.centimeter
    length_in_miles = length_in_centimeters.to(ureg.mile)
    return length_in_miles.magnitude
