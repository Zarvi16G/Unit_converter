from pint import UnitRegistry

# Inicializa el registro de unidades
ureg = UnitRegistry()

def length_km_to_mm(length):
    """Convierte de kilómetros a milímetros."""
    length_in_kilometers = length * ureg.kilometer
    length_in_millimeters = length_in_kilometers.to(ureg.millimeter)
    return length_in_millimeters.magnitude

def length_km_to_cm(length):
    """Convierte de kilómetros a centímetros."""
    length_in_kilometers = length * ureg.kilometer
    length_in_centimeters = length_in_kilometers.to(ureg.centimeter)
    return length_in_centimeters.magnitude

def length_km_to_m(length):
    """Convierte de kilómetros a metros."""
    length_in_kilometers = length * ureg.kilometer
    length_in_meters = length_in_kilometers.to(ureg.meter)
    return length_in_meters.magnitude

def length_km_to_km(length):
    """Convierte de kilómetros a kilómetros (sin cambio)."""
    length_in_kilometers = length * ureg.kilometer
    return length_in_kilometers.magnitude  # Devolver el mismo valor

def length_km_to_inch(length):
    """Convierte de kilómetros a pulgadas."""
    length_in_kilometers = length * ureg.kilometer
    length_in_inches = length_in_kilometers.to(ureg.inch)
    return length_in_inches.magnitude

def length_km_to_foot(length):
    """Convierte de kilómetros a pies."""
    length_in_kilometers = length * ureg.kilometer
    length_in_feet = length_in_kilometers.to(ureg.foot)
    return length_in_feet.magnitude

def length_km_to_yard(length):
    """Convierte de kilómetros a yardas."""
    length_in_kilometers = length * ureg.kilometer
    length_in_yards = length_in_kilometers.to(ureg.yard)
    return length_in_yards.magnitude

def length_km_to_mile(length):
    """Convierte de kilómetros a millas."""
    length_in_kilometers = length * ureg.kilometer
    length_in_miles = length_in_kilometers.to(ureg.mile)
    return length_in_miles.magnitude