from pint import UnitRegistry

ureg = UnitRegistry()

def length_m_to_mm(length):
    """Convierte de metros a milímetros."""
    length_in_meters = length * ureg.meter
    length_in_millimeters = length_in_meters.to(ureg.millimeter)
    return length_in_millimeters.magnitude

def length_m_to_cm(length):
    """Convierte de metros a centímetros."""
    length_in_meters = length * ureg.meter
    length_in_centimeters = length_in_meters.to(ureg.centimeter)
    return length_in_centimeters.magnitude

def length_m_to_m(length):
    """Convierte de metros a metros (sin cambio)."""
    length_in_meters = length * ureg.meter
    return length_in_meters.magnitude  

def length_m_to_km(length):
    """Convierte de metros a kilómetros."""
    length_in_meters = length * ureg.meter
    length_in_kilometers = length_in_meters.to(ureg.kilometer)
    return length_in_kilometers.magnitude

def length_m_to_inch(length):
    """Convierte de metros a pulgadas."""
    length_in_meters = length * ureg.meter
    length_in_inches = length_in_meters.to(ureg.inch)
    return length_in_inches.magnitude

def length_m_to_foot(length):
    """Convierte de metros a pies."""
    length_in_meters = length * ureg.meter
    length_in_feet = length_in_meters.to(ureg.foot)
    return length_in_feet.magnitude

def length_m_to_yard(length):
    """Convierte de metros a yardas."""
    length_in_meters = length * ureg.meter
    length_in_yards = length_in_meters.to(ureg.yard)
    return length_in_yards.magnitude

def length_m_to_mile(length):
    """Convierte de metros a millas."""
    length_in_meters = length * ureg.meter
    length_in_miles = length_in_meters.to(ureg.mile)
    return length_in_miles.magnitude