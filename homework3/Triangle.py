from Shape import Shape

class Triangle(Shape):
    __slots__ = ("_base", "_height") # inherrit _name and _area from Shape

    def __init__(self, name: str, base: float, height: float) -> None:
        super().__init__(name) # call shape __init__
        self._base = base
        self._height = height
        self._area = 0.5 * base * height # calc area


    def getBase(self) -> float:
        return self._base

    def getHeight(self) -> float:
        return self._height
    
    def setBase(self, base: float) -> None:
        self._base = base
        self._area = 0.5 * base * self._height # update new area

    def setHeight(self, height: float) -> None:
        self._height = height
        self._area = 0.5 * self._base * height # update new area

    def __str__(self) -> str:
        return f"Triangle {self._name}: base = {self._base} height = {self._height} area = {self._area}"

    def __eq__(self, other: "Triangle") -> bool:
        if not isinstance(other, Triangle):
            return False
        return self._base == other._base and self._height == other._height

def main() -> None:
    t1 = Triangle("tommy", 4.0, 5.0)
    print(t1) #test __str__
    print(f"base: {t1.getBase()}")
    print(f"height: {t1.getHeight()}")
    print(f"area: {t1.getArea()}")

    t1.setBase(6.0)
    t1.setHeight(7.0)
    print(f"updated base: {t1.getBase()}")
    print(f"updated height: {t1.getHeight()}")
    print(f"updated area: {t1.getArea()}")

    t2 = Triangle("timmy", 6.0, 7.0)
    print(f"t1 == t2?: {t1 == t2}")

    t3 = Triangle("cuppo", 2.0, 1.0)
    print(t3) #test __str__
    print(f"base: {t3.getBase()}")
    print(f"height: {t3.getHeight()}")
    print(f"area: {t3.getArea()}")

    t3.setBase(5.0)
    t3.setHeight(2.0)
    print(f"updated base: {t3.getBase()}")
    print(f"updated height: {t3.getHeight()}")
    print(f"updated area: {t3.getArea()}")

if __name__ == "__main__":
    main()