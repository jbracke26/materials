#      - main.py
#          * Import classes from shapes.py
#          * Import helper functions from utils.py
#          * Allow user to create shapes (input dimensions)
#          * Print area and descriptions

import utils
import shapes

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

class Rectangle:
    """
    A rectangle shape defined by width and height.

    Attributes:
        width (int): how wide the rectangle is
        height (int): how tall the rectangle is
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        """
        Compute the area of this rectangle.

        Returns:
            int: the area (width * height)
        """
        return self.width * self.height

    def describe(self) -> None:
        """
        Print a description of the rectangle.

        Returns:
            None
        """
        print(f"Rectangle {self.width} by {self.height} has area {self.area()}")


class Circle:
    """
    A circle shape defined by radius.

    Attributes:
        radius (int): how big the circle is
    """

    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> float:
        """
        Compute the area of this circle.

        Returns:
            float: the area (pi * radius^2)
        """
        return 3.14159 * self.radius ** 2

    def describe(self) -> None:
        """
        Print a description of the circle.

        Returns:
            None
        """
        print(f"Circle {self.radius} has area {self.area()}")

class Triangle:
    """
    A triangle shape defined by base and height.

    Attributes:
        base (int): how wide the base of the triangle is
        height (int): how tall the triangle is
    """

    def __init__(self, base: int, height: int):
        self.base = base
        self.height = height

    def area(self) -> float:
        """
        Compute the area of this triangle.

        Returns:
            float: the area (0.5 * base * height)
        """
        return 0.5 * self.base * self.height

    def describe(self) -> None:
        """
        Print a description of the triangle.

        Returns:
            None
        """
        print(f"Triangle {self.base} by {self.height} has area {self.area()}")

class Square:
    """
    A square shape defined by width and height.

    Attributes:
        width (int): how wide the square is
        height (int): how tall the square is
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        """
        Compute the area of this square.

        Returns:
            int: the area (width * height)
        """
        return self.width * self.height

    def describe(self) -> None:
        """
        Print a description of the square.

        Returns:
            None
        """
        print(f"Square {self.width} by {self.height} has area {self.area()}")

if __name__ == "__main__":
    # Allow user to create shapes (input dimensions)
    # Print area and descriptions
    shape = input("Enter shape (rectangle, circle, triangle, square): ")
    if shape == "rectangle":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        rectangle = Rectangle(width, height)
        rectangle.describe()
    elif shape == "circle":
        radius = int(input("Enter radius: "))
        circle = Circle(radius)
        circle.describe()
    elif shape == "triangle":
        base = int(input("Enter base: "))
        height = int(input("Enter height: "))
        triangle = Triangle(base, height)
        triangle.describe()
    elif shape == "square":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        square = Square(width, height)
        square.describe()
    else:
        print("Invalid shape")