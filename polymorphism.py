class Shape:
    __slops__ = ("_name", "_area")
    def __init__(self, name: str) -> None:
        self._name = name
        self._area = 0

    def __str__(self) -> str:
        return f"Shape {self._name}: area = {self._area}"
    
    def foobar(self) -> str: return "foobar"

class Triangle(Shape):
    __slots__ = ("_base", "_height")
    
    def __init__(self, name: str, base: float, height: float) -> None:
        super().__init__(name)
        self._base = base
        self._height = height
        self._area = 0.5 * base * height
    def foobar:(self) -> str: return "triangle override"
    
class Rectangle(Shape):
    __slots__ = ("_width", "_height")

    def __init__(self, name: str, width: float, height: float) -> None:
        super().__init__(name)
        self._width = width
        self._height = height
        self._area = width * height
    def __str__(self) -> str:
        return f"Rectangle {self._name}: params = {self._width}, {self._height}"

def processShape(shape: Shape) -> None:
    print(shape.foobar())


def main() -> None:
    t = Triangle("tam", 3.0, 4.5)
    print(t)

    r = Rectangle("rango", 2, 3)
    print(r)

if __name__ == "__main__":
    main()