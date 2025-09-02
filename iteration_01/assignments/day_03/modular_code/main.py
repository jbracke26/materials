#      - main.py
#          * Import classes from shapes.py
#          * Import helper functions from utils.py
#          * Allow user to create shapes (input dimensions)
#          * Print area and descriptions

from shapes import Rectangle, Circle, Triangle
from utils import convert_area


def prompt_int(message):
    return int(input(message))


if __name__ == "__main__":
    # Allow user to create shapes (input dimensions)
    # Print area and descriptions
    shape = input("Enter shape (rectangle, circle, triangle): ").strip().lower()

    creators = {
        "rectangle": lambda: Rectangle(
            prompt_int("Enter width (cm): "), prompt_int("Enter height (cm): ")
        ),
        "circle": lambda: Circle(prompt_int("Enter radius (cm): ")),
        "triangle": lambda: Triangle(
            prompt_int("Enter base (cm): "), prompt_int("Enter height (cm): ")
        ),
    }

    if shape not in creators:
        print("Invalid shape")
    else:
        obj = creators[shape]()
        # Base area will be in cm^2 because inputs are in cm
        area_cm2 = obj.area()
        target_unit = input("Output area unit (cm2/m2): ").strip().lower()
        if target_unit not in ("cm2", "m2"):
            target_unit = "cm2"
        area_out = convert_area(area_cm2, "cm2", target_unit)
        print(f"{shape.title()} area: {area_out} {target_unit}")