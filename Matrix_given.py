from __future__ import annotations  # so we can use Matrix as a type hint

class Matrix:
    __slots__ = ("_num_rows", "_num_cols", "_data")

    # for now, just handle a creation such as
    #     m = Matrix(2, 3, [8,6,7,5,3,9])
    def __init__(self, num_rows: int, num_cols: int, data: list[int]) -> None:
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._data = []
        for r in range(num_rows):
            row_data = []  # build one row at a time
            for c in range(num_cols):
                #row_data.append( data[c] )
                index = (r * num_cols) + c
                row_data.append( data[index] )
            self._data.append(row_data)

    def __str__(self) -> str:
        return str(self._data)  # not what you ultimately want to do...

def main() -> None:
    m = Matrix(2, 3, [4, 33, 22, 11, 19, 7])
    print(m)

    import random
    m = Matrix(3, 4, [random.randint(1,99) for i in range(12)])
    print(m)

# wrap the call to main so it won't be executed whenever
# this file is imported elsewhere
if __name__ == "__main__":
    main()