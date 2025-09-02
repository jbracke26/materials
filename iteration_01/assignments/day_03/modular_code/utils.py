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
