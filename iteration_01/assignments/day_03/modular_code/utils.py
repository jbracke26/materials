#      - utils.py
#          * Create helper functions, e.g., convert cm^2 to m^2
#          * Compare areas of two shapes

def  convert_cm2_to_m2(area_cm2):
    area_m2 = area_cm2 / 10000
    return area_m2

def compare_areas(area1, area2):
    if area1 > area2:
        return 1
    elif area1 < area2:
        return -1
    else:
        return 0

# New: generic area unit conversions
# Supported units: "cm2", "m2"

_UNIT_TO_M2 = {
    "m2": 1.0,
    "cm2": 1.0 / 10000.0,
}


def convert_area(value, from_unit, to_unit):
    """
    Convert an area quantity between supported units.

    Parameters:
        value (float): numeric area value
        from_unit (str): one of "cm2", "m2"
        to_unit (str): one of "cm2", "m2"

    Returns:
        float: converted value in the requested unit
    """
    if from_unit not in _UNIT_TO_M2 or to_unit not in _UNIT_TO_M2:
        raise ValueError("Unsupported unit. Use 'cm2' or 'm2'.")
    value_in_m2 = float(value) * _UNIT_TO_M2[from_unit]
    if to_unit == "m2":
        return value_in_m2
    # back to cm2
    return value_in_m2 / _UNIT_TO_M2["cm2"]
