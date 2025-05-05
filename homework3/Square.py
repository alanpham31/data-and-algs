from Rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, name: str, side: float) -> None:
        super().__init__(name, side, side)
    
    def setWidth(self, width: float) -> None:
        super().setWidth(width)
        super().setHeight(width)
        self._area = width * width # new area
    
    def setHeight(self, height: float) -> None:
        super().getHeight(height)
        super().getWidth(height)
        self._area = height * height # new area

    def __str__(self) -> str:
        return f"square {self._name}: side = {self._width} area = {self._area}"
    
def main() -> None:
    s1 = Square("sally", 5.0)
    print(s1)
    print(f"side: {s1.getWidth()}")
    print(f"area: {s1.getArea()}")
    print(f"perimeter: {s1.getPerimeter()}")

    s1.setWidth(6.0)
    print(f"new side: {s1.getWidth()}")
    print(f"new area: {s1.getArea()}")

    s2 = Square("silly", 6.0)
    print(f"s1 == s2?: {s1 == s2}")

    s3 = Square("viktor", 4.0)
    print(s3)
    print(f"side: {s3.getWidth()}")
    print(f"area: {s3.getArea()}")
    print(f"perimeter: {s3.getPerimeter()}")

    s3.setWidth(2.0)
    print(f"new side: {s3.getWidth()}")
    print(f"new area: {s3.getArea()}")

if __name__ == "__main__":
    main()