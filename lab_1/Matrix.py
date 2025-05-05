class Matrix:
    __slots__ = ("_num_rows", "_num_cols", "_data")

    def __init__(self, 
                 rows: int = 0, 
                 cols: int = 0, 
                 data: list[int] = None, 
                 *, 
                 filename: str = None) -> None:
        if filename:
            self._initialize_file(filename)
        else:
            self._initialize_data(rows, cols, data)
            
    # helper method - input
    def _initialize_data(self, rows, cols, data):
        if data is None or len(data) != rows * cols:
            raise ValueError("length of data does not match dimensions")
        self._num_rows = rows
        self._num_cols = cols
        self._data = []
        for r in range(rows):
            row_data = []  # build one row at a time
            for c in range(cols):
                #row_data.append(data[c])
                index = (r * cols) + c
                row_data.append(data[index])
            self._data.append(row_data)

    # helper method - extract file
    def _initialize_file(self, filename):
        with open(filename, "r") as file:
            lines = [list(map(int, line.split()) for line in file)]
        
        row_len = len(lines[0])
        if any(len(row) != row_len for row in lines):
            raise ValueError("row length inconsistent in file")
        
        self._num_rows = len(lines)
        self._num_cols = row_len
        self._data = []
        for r in range(len(lines)):
            row_data = []  # build one row at a time
            for c in range(row_len):
                #row_data.append(data[c])
                index = (r * row_len) + c
                row_data.append(lines)
            self._data.append(row_data)

    def __str__(self):
        col_width = max(len(str(num)) for row in self._data for num in row)        
        result = []
        for row in self._data:
            formatted_row = "  ".join(f"{num:>{col_width}}" for num in row)
            result.append(f"| {formatted_row} |")
        return "\n".join(result)

    def __getitem__(self, row_col):
        row, col = row_col
        if (row < 0 or 
            row >= self._num_rows or 
            col < 0 or 
            col >= self._num_cols):
            raise IndexError("matrix index out of range")
        return self._data[row][col]

    def __eq__ (self, other):
        if not isinstance(other, Matrix):
            raise TypeError("only compare with another matrix")
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
        if (self._num_rows != other._num_rows or
            self._num_cols != other._num_cols):
            raise ValueError("matrix dimensions must match")
        new_data = [
            [self._data[i][j] + other._data[i][j] for i in range(self._num_rows)]
            for j in range(self._num_cols)
        ]
        return Matrix(self._num_rows, 
                      self._num_cols, 
                      new_data)
    
    def __mul__(self, other):
        if self._num_cols != other._num_rows:
            raise ValueError ("# of cols in 1st matrix must equal # of rows in 2nd matrix")
        new_data = [
            [sum(self._data[i][k] * other._data[k][j] for k in range(self._num_cols))
            for j in range(other._num_cols)]
            for i in range(self._num_rows)
        ]
        return Matrix(self._num_rows, 
                      other._num_cols, 
                      new_data)
    
    def transpose(self):
        new_data = [
            [self._data[j][i] for j in range(self._num_rows)]
            for i in range(self._num_cols)
        ]
        return Matrix(self._num_cols, self._num_rows, new_data)


def main():
    m1 = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
    m2 = Matrix(2, 3, [6, 5, 4, 3, 2, 1])
    m_2x3 = Matrix(2, 3, [12, 234, 3456, 12345, 23, 3])
    m3 = Matrix(2, 3, [1, 2, 3, 4, 5, 6])

    # Matrix test display
    print("matrix 1:")
    print(m1)
    print("matrix 2:")
    print(m2)

    # Testing __getitem__
    print("matrix 2x3:")
    print(m_2x3)
    print("item at (1,1):", m_2x3[1, 1])

    # Testing equality check
    print("matrix 3")
    print(m3)
    print("matrix 1 == matrix 3:", m1 == m3)

    # Testing addition function
    m4 = m1 + m2
    print("Addition Result:")
    print(m4)

    # Uncomment for file reading test
    '''
    try:

    except FileNotFoundError:
        raise ValueError("file not found")'''
    m_file = Matrix(filename="extract_me.txt")
    print("Matrix from file:")
    print(m_file)

if __name__ == "__main__":
    main()

