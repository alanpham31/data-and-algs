class Matrix:
    __slots__ = ("_num_rows", "_num_cols", "_data")

    def __init__(self, 
                 rows: int = 0, 
                 cols: int = 0, 
                 data: list[int] = None, 
                 *, 
                 filename: str = None) -> None:
        '''
        initialize a matrix object
        inputs:
            - rows: number of rows in matrix
            - cols: number of columns in matrix
            - data: 2d list of intergers with file name to load matrix data 

        behavior:
            - if filename given, matrix initialized from file
            - else if the matrix is initialized via rows, cols, and data
            - else ValueError (FileNotFound error)
        '''
        if filename:
            self._initialize_file(filename)
        else:
            self._initialize_data(rows, cols, data)
            
    # helper method - input
    def _initialize_data(self, rows, cols, data):
        '''
        helper method to initialize matrix data from list
        inputs:
            - rows: number of rows in the matrix
            - cols: numeber of columns in the matrix
            - data: list of integers representing the matrix data
        behavior:
            - converts list into 2d list representing matrix
            - raises ValueError if length of data != match dimensions
        '''
        if data is None or len(data) != rows * cols:
            raise ValueError("length of data does not match dimensions")
        self._num_rows = rows
        self._num_cols = cols
        self._data = []
        for r in range(rows):
            row_data = []  # build one row at a time
            for c in range(cols):
                index = (r * cols) + c
                row_data.append(data[index])
            self._data.append(row_data)

    # helper method - extract file
    def _initialize_file(self, filename):
        '''
        helper method to initialize data from file
        inputs:
            - filename: string with name opf file to load matrix data from
        behavior:
            - reads file and puts contents into 2d list 
            - raises ValueError if file does not have consistent row length
        '''
        with open(filename, "r") as file:
            lines = [list(map(int, line.split())) for line in file]
        
        row_len = len(lines[0])
        if any(len(row) != row_len for row in lines):
            raise ValueError("row length inconsistent in file")
        
        self._num_rows = len(lines)
        self._num_cols = row_len
        self._data = lines

    def __str__(self):
        '''
        returns string representing matrix in specified format
        output:
            - formatted string with matrix
        behavior:
            - matrix is shown with rows and columns aligned
        '''
        col_width = max(len(str(num)) for row in self._data for num in row)        
        result = []
        for row in self._data:
            formatted_row = "  ".join(f"{num:>{col_width}}" for num in row)
            result.append(f"| {formatted_row} |")
        return "\n".join(result)

    def __getitem__(self, row_col):
        '''
        returns element at specified row and column
        inputs:
            - row_col: tuple (row, column) with position of element
        output:
            - element at the specified position
        behavior:
            - raises IndexError if the row or column is out of bounds
        '''
        row, col = row_col
        if (row < 0 or 
            row >= self._num_rows or 
            col < 0 or 
            col >= self._num_cols):
            raise IndexError("matrix index out of range")
        return self._data[row][col]

    def __eq__ (self, other):
        '''
        compares two matrices for equality
        input: 
            - other: another matrix object to compare
        output:
            - true if matrices are equal 
            - false otherwise
        behavior:
            - raises TypeError if other is not matrix object
        '''
        if not isinstance(other, Matrix):
            raise TypeError("only compare with another matrix")
        return (
            self._num_rows == other._num_rows and 
            self._num_cols == other._num_cols and 
            self._data == other._data
        )
    
    def getNumRows(self) -> int:
        '''
        returns number of rows in the matrix
        output:
            - integer with number of rows
        '''
        return self._num_rows
    
    def getNumCols(self) -> int:
        '''
        returns number of columns in the matrix
        output:
            - integer with number of columns
        '''
        return self._num_cols
    
    def __add__(self, other):
        '''
        adds two matrices
        inputs:
            - other: another matrix object to add
        outputs:
            - new matrix object representing sum of two matrices
        behavior:
            - raises ValueError if matrices have different dimensions
        '''
        if (self._num_rows != other._num_rows or
            self._num_cols != other._num_cols):
            raise ValueError("matrix dimensions must match")
        new_data = [
            self._data[i][j] + other._data[i][j]
            for i in range(self._num_rows)
            for j in range(self._num_cols)
        ]
        return Matrix(self._num_rows, self._num_cols, new_data)
    
    def __mul__(self, other):
        '''
        multiplies two matrices
        inputs:
            - other: another matrix object to multiply
        outputs:
            - new matrix object that represents product of the two matrices
        behavior:
            - raises ValueError if number of columns in the first matrix does not match 
            number of rows in the second matrix
        '''
        if self._num_cols != other._num_rows:
            raise ValueError("# of cols in 1st matrix must equal # of rows in 2nd matrix")
        new_data = [
            [sum(self._data[i][k] * other._data[k][j] for k in range(self._num_cols))
            for j in range(other._num_cols)]
            for i in range(self._num_rows)
        ]
        return Matrix(self._num_rows, other._num_cols, new_data)
    
    def transpose(self):
        '''
        transpose matrix
        output:
            - new matrix object representing transpose of original matrix
        behavior:
            - rows and columns of the original matrix are swapped
        '''
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

    # Testing file reading
    try:
        m_file = Matrix(filename="extract_me.txt")
        print("Matrix from file:")
        print(m_file)
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()