class Matrix:
    __slots__ = ("_num_rows", "_num_cols", "_data")

    def __init__(self, 
                 rows: int = 0, 
                 cols: int = 0, 
                 data: list[int] = None, 
                 *, 
                 filename=None) -> None:
        if filename:
            self._initialize_file(filename)
        else:
            self._initialize_data(rows, cols, data)

    # helper method
    def _initialize_data(self, rows, cols, data):
        if data is None or len(data) != rows * cols:
            raise ValueError("Length of data does not match dimensions")
        self._num_rows = rows
        self._num_cols = cols
        self._data = []
        for r in range(rows):
            row_data = []  # build one row at a time
            for c in range(cols):
                #row_data.append( data[c] )
                index = (r * cols) + c
                row_data.append( data[index] )
            self._data.append(row_data)

    # helper method
    def _initialize_file(self, filename):
        try:
            with open(filename, "r") as file:
                lines = [list(map(int, line.split())) for line in file]
            
            row_len = len(lines[0])
            if any(len(row) != row_len for row in lines):
                raise ValueError("Row length inconsistent in file")
            
            self._num_rows = len(lines)
            self._num_cols = row_len
            self._data = lines

        except FileNotFoundError:
            raise ValueError("File not found")

    def __str__(self):
        col_width = max(len(str(num)) for row in self._data for num in row)        
        result = []
        for row in self._data:
            formatted_row = "  ".join(f"{num:>{col_width}}" for num in row)
            result.append(f"| {formatted_row} |")
        return "\n".join(result)

    def __getitem__(self, row_col):
        row, col = row_col
        if row < 0 or row >= self._num_rows or col < 0 or col >= self._num_cols:
            raise IndexError("Matrix index out of range")
        return self._data[row][col]

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Only compare with another matrix")
        return (
            self._num_rows == other._num_rows and 
            self._num_cols == other._num_cols and 
            self._data == other._data
        )
    
    def getNumRows(self) -> int:
        return self._num_rows
    
    def getNumCols(self) -> int:
        return self._num_cols
    
    def __add__(self, other):
        if self._num_rows != other._num_rows or self._num_cols != other._num_cols:
            raise ValueError("Matrix dimensions must match to add")
        
        new_data = [
            self._data[i][j] + other._data[i][j]
            for i in range(self._num_rows)
            for j in range(self._num_cols)
        ]
        
        return Matrix(self._num_rows, self._num_cols, new_data)
    

def main():
    m1 = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
    m2 = Matrix(2, 3, [6, 5, 4, 3, 2, 1])
    m_2x3 = Matrix(2, 3, [12, 234, 3456, 12345, 23, 3])
    m3 = Matrix(2, 3, [1, 2, 3, 4, 5, 6])

    # Matrix test display
    print("Matrix 1:")
    print(m1)
    print("Matrix 2:")
    print(m2)

    # Testing __getitem__
    print("Matrix m_2x3:")
    print(m_2x3)
    print("Element at (1,1):", m_2x3[1, 1])  # Corrected __getitem__ usage

    # Testing equality check
    print("Matrix 1 == Matrix 3:", m1 == m3)

    # Testing addition function
    m4 = m1 + m2
    print("Addition Result:")
    print(m4)

    # Uncomment for file reading test
    m_file = Matrix(filename="extract_me.txt")
    print(f"Matrix from file:")
    print(m_file)

if __name__ == "__main__":
    main()
