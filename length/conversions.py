from pint import UnitRegistry
from . import centimeter_to, kilometer_to, meter_to, mile_to, yard_to, inch_to, foot_to, millimeter_to

ureg = UnitRegistry()

def type_unit_form(length, unit_from, unit_to):
    if unit_from == 'meter':
        return length_meter_to(length, unit_to)
    elif unit_from == 'kilometer':
        return length_kilometer_to(length, unit_to)
    elif unit_from == 'centimeter':
        return length_centimeter_to(length, unit_to)
    elif unit_from == 'millimeter':
        return length_millimeter_to(length, unit_to)
    elif unit_from == 'yard':
        return length_yard_to(length, unit_to)
    elif unit_from == 'inch':
        return length_inch_to(length, unit_to)
    elif unit_from == 'foot':
        return length_foot_to(length, unit_to)
    elif unit_from == 'mile':
        return length_mile_to(length, unit_to)
    

# Meters to other units
def length_meter_to(length, unit_to):
    if unit_to == 'kilometer':
        return meter_to.length_m_to_km(length)
    elif unit_to == 'millimeter':
        return meter_to.length_m_to_mm(length)
    elif unit_to == 'centimeter':
        return meter_to.length_m_to_cm(length)
    elif unit_to == 'inch':
        return meter_to.length_m_to_inch(length)
    elif unit_to == 'foot':
        return meter_to.length_m_to_foot(length)
    elif unit_to == 'yard':
        return meter_to.length_m_to_yd(length)
    elif unit_to == 'mile':
        return meter_to.length_m_to_mile(length)
    else:
        return meter_to.length_m_to_m(length)

# Kilometers to other units
def length_kilometer_to(length, unit_to):
    if unit_to == 'meter':
        return kilometer_to.length_km_to_m(length)
    elif unit_to == 'millimeter':
        return kilometer_to.length_km_to_mm(length)
    elif unit_to == 'centimeter':
        return kilometer_to.length_km_to_cm(length)
    elif unit_to == 'inch':
        return kilometer_to.length_km_to_inch(length)
    elif unit_to == 'foot':
        return kilometer_to.length_km_to_foot(length)
    elif unit_to == 'yard':
        return kilometer_to.length_km_to_yd(length)
    elif unit_to == 'mile':
        return kilometer_to.length_km_to_mile(length)
    else:
        return kilometer_to.length_km_to_km(length)

# Centimeters to other units
def length_centimeter_to(length, unit_to):
    if unit_to == 'meter':
        return centimeter_to.length_cm_to_m(length)
    elif unit_to == 'millimeter':
        return centimeter_to.length_cm_to_mm(length)
    elif unit_to == 'kilometer':
        return centimeter_to.length_cm_to_km(length)
    elif unit_to == 'inch':
        return centimeter_to.length_cm_to_inch(length)
    elif unit_to == 'foot':
        return centimeter_to.length_cm_to_foot(length)
    elif unit_to == 'yard':
        return centimeter_to.length_cm_to_yd(length)
    elif unit_to == 'mile':
        return centimeter_to.length_cm_to_mile(length)
    else:
        return centimeter_to.length_cm_to_cm(length)

# Millimeters to other units
def length_millimeter_to(length, unit_to):
    if unit_to == 'meter':
        return millimeter_to.length_mm_to_m(length)
    elif unit_to == 'centimeter':
        return millimeter_to.length_mm_to_cm(length)
    elif unit_to == 'kilometer':
        return millimeter_to.length_mm_to_km(length)
    elif unit_to == 'inch':
        return millimeter_to.length_mm_to_inch(length)
    elif unit_to == 'foot':
        return millimeter_to.length_mm_to_foot(length)
    elif unit_to == 'yard':
        return millimeter_to.length_mm_to_yd(length)
    elif unit_to == 'mile':
        return millimeter_to.length_mm_to_mile(length)
    else:
        return millimeter_to.length_mm_to_mm(length)

# Yards to other units
def length_yard_to(length, unit_to):
    if unit_to == 'meter':
        return yard_to.length_yd_to_m(length)
    elif unit_to == 'millimeter':
        return yard_to.length_yd_to_mm(length)
    elif unit_to == 'centimeter':
        return yard_to.length_yd_to_cm(length)
    elif unit_to == 'kilometer':
        return yard_to.length_yd_to_km(length)
    elif unit_to == 'inch':
        return yard_to.length_yd_to_inch(length)
    elif unit_to == 'foot':
        return yard_to.length_yd_to_foot(length)
    elif unit_to == 'mile':
        return yard_to.length_yd_to_mile(length)
    else:
        return yard_to.length_yd_to_yd(length)

# Inches to other units
def length_inch_to(length, unit_to):
    if unit_to == 'meter':
        return inch_to.length_inch_to_m(length)
    elif unit_to == 'millimeter':
        return inch_to.length_inch_to_mm(length)
    elif unit_to == 'centimeter':
        return inch_to.length_inch_to_cm(length)
    elif unit_to == 'kilometer':
        return inch_to.length_inch_to_km(length)
    elif unit_to == 'yard':
        return inch_to.length_inch_to_yd(length)
    elif unit_to == 'foot':
        return inch_to.length_inch_to_foot(length)
    elif unit_to == 'mile':
        return inch_to.length_inch_to_mile(length)
    else:
        return inch_to.length_inch_to_inch(length)

# Feet to other units
def length_foot_to(length, unit_to):
    if unit_to == 'meter':
        return foot_to.length_foot_to_m(length)
    elif unit_to == 'millimeter':
        return foot_to.length_foot_to_mm(length)
    elif unit_to == 'centimeter':
        return foot_to.length_foot_to_cm(length)
    elif unit_to == 'kilometer':
        return foot_to.length_foot_to_km(length)
    elif unit_to == 'yard':
        return foot_to.length_foot_to_yd(length)
    elif unit_to == 'inch':
        return foot_to.length_foot_to_inch(length)
    elif unit_to == 'mile':
        return foot_to.length_foot_to_mile(length)
    else:
        return foot_to.length_foot_to_foot(length)

# Miles to other units
def length_mile_to(length, unit_to):
    if unit_to == 'meter':
        return mile_to.length_mile_to_m(length)
    elif unit_to == 'millimeter':
        return mile_to.length_mile_to_mm(length)
    elif unit_to == 'centimeter':
        return mile_to.length_mile_to_cm(length)
    elif unit_to == 'kilometer':
        return mile_to.length_mile_to_km(length)
    elif unit_to == 'yard':
        return mile_to.length_mile_to_yd(length)
    elif unit_to == 'inch':
        return mile_to.length_mile_to_inch(length)
    elif unit_to == 'foot':
        return mile_to.length_mile_to_foot(length)
    else:
        return mile_to.length_mile_to_mile(length)
