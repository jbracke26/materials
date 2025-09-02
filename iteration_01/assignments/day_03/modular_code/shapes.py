# 2. Inside that folder, create three files:
#      - shapes.py
#          * Define at least three classes: Rectangle, Circle, Triangle
#          * Each class should have attributes, area() method, and describe() method

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

