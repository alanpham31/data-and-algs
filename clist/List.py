from ctypes import *

class List:
    __slots__ = ("_array", "_num_entries", "_capacity")

    def __init__(self) -> None:
        self._num_entries = 0

        self._capacity = 10
        ArrayType = self._capacity * c_int
        self._array = ArrayType()

    def append(self, item: int) -> None:
        self._array[self._num_entries] = item
        self._num_entries += 1
    
    def __str__(self) -> str:
        value = '[]'
        for i in range(self._num_entries):
            value += str(self._array[i]) + ","
        value = value[:-1] + "]"
        return value


def main() -> None:
    l = List()

main()