from Shape import Shape

class Rectangle(Shape):
    __slots__ = ("_width", "_height") # inherit _name and _area from Shape

    def __init__(self, name: str, width: float, height: float) -> None:
        super().__init__(name) 
        self._width = width
        self._height = height
        self._area = width * height # calc area

    def getWidth(self) -> float:
        return self._width
    
    def getHeight(self) -> float:
        return self._height
    
    def setWidth(self, width: float) -> None:
        self._width = width
        self._area = width * self._height # update new area

    def setHeight(self, height: float) -> None:
        self._height = height
        self._area = height * self._width # update new area

    def getPerimeter(self) -> float:
        return 2 * (self._width + self._height)
    
    def __str__(self) -> str:
        return f"Rectangle {self._name}: width = {self._width} height = {self._height} area = {self._area}"
    
    def __eq__(self, other: "Rectangle") -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self._width == other._width and self._height == other._height
    
def main() -> None:
    r1 = Rectangle("robby", 4.0, 5.0)
    print(r1)
    print(f"width: {r1.getWidth()}")
    print(f"height: {r1.getHeight()}")
    print(f"area: {r1.getArea()}")
    print(f"perimeter: {r1.getPerimeter()}")

    r1.setWidth(6.0)
    r1.setHeight(7.0)
    print(f"new width: {r1.getWidth()}")
    print(f"new height: {r1.getHeight()}")
    print(f"updated area: {r1.getArea()}")

    r2 = Rectangle("ribby", 6.0, 7.0)
    print(f"r1 == r2?: {r1 == r2}")

    r3 = Rectangle("tok", 12.0, 1.0)
    print(r3)
    print(f"width: {r3.getWidth()}")
    print(f"height: {r3.getHeight()}")
    print(f"area: {r3.getArea()}")
    print(f"perimeter: {r3.getPerimeter()}")

    r3.setWidth(2.0)
    r3.setHeight(1.0)
    print(f"new width: {r3.getWidth()}")
    print(f"new height: {r3.getHeight()}")
    print(f"updated area: {r3.getArea()}")

if __name__ == "__main__":
    main()