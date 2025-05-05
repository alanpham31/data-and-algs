from Shape import Shape
import math  # for math.pi

class Circle(Shape):
    __slots__ = ("_radius")  # will inherit _name, _area from Shape

    def __init__(self, name: str, radius: float) -> None:
        super().__init__(name)    # callling __init__ inside Shape; needs name arg

        # the Shape is now set up, so finish setting up circle
        self._radius = radius
        self._area   = math.pi * radius**2  # ok to access _area b/c Circle is-a Shape

    ''' finish the methods necessary for Circle '''


    def getRadius(self) -> float:
        return self._radius

    def setRadius(self, radius: float) -> None:
        self._radius = radius
        self._area = math.pi * radius**2 # update new area
    
    def getPerimeter(self) -> float:
        return 2 * math.pi * self._radius
    
    def __str__(self) -> str:
        return f"circle {self._name}: radius = {self._radius} area = {self._area}"

def main() -> None:
    c1 = Circle("sammy", 3)
    print(c1)  # unless you override __str__ above, this will use __str__ from Shape
    print(f"name of c1: {c1.getName()}")
    print(f"area of c1: {c1.getArea()}")
    print(f"is c1 a Circle? {isinstance(c1, Circle)}")

    c1.setRadius(4.0)
    print(f"Updated Radius: {c1.getRadius()}")
    print(f"Updated Perimeter: {c1.getPerimeter()}")
    print(f"Updated Area: {c1.getArea()}")

    c2 = Circle("sammy", 3)
    print(f"c1 == c2? {c1 == c2}")  # do you need to override __eq__ inside Circle?

    c3 = Circle("tik", 12.1)
    print(c3)
    print(f"name of c1: {c3.getName()}")
    print(f"area of c1: {c3.getArea()}")
    print(f"is c1 a Circle? {isinstance(c3, Circle)}")

    c3.setRadius(88.0)
    print(f"Updated Radius: {c3.getRadius()}")
    print(f"Updated Perimeter: {c3.getPerimeter()}")
    print(f"Updated Area: {c3.getArea()}")


if __name__ == "__main__":
    main()