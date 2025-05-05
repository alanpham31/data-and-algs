from __future__ import annotations

class Shape:
    __slots__ = ("_name", "_area")

    def __init__(self, name: str) -> None:
        self._name: str   = name
        self._area: float = 0.0

    # overriding the __str__ inherted from object
    def __str__(self) -> str:   
        return f"Shape {self._name}: area = {self._area}"

    def getArea(self) -> float: return self._area
    def getName(self) -> str:   return self._name

    # overriding the __eq__ inherited from object
    def __eq__(self, other: Shape) -> bool:
        # calling __eq__ in str and in float respectively
        return self._name == other._name and self._area == other._area


def main() -> None:
    s1 = Shape("blob")
    s2 = Shape("blob")
    s3 = s2

    print(f"is s1 a Shape? {isinstance(s1, Shape)}")

    print(f"s1 == s2: {s1 == s2}")
    print(f"s2 == s3: {s2 == s3}")

    print(s1)
    #print(f"Area of {s1._name} is {s1._area}")  # don't access private inst. vars1
    print(f"Area of {s1.getName()} is {s1.getArea()}")

if __name__ == "__main__":
    main()
