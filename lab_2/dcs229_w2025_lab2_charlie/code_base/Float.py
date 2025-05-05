from Number import Number

######################################################################
class Float(Number):
    __slots__ = ("_digits")

    def __init__(self, value: float | int, digits: int = 2) -> None:
        ''' initializer method for Float class
        Parameter:
            value: a float or integer
            digits: an integer representing # of digits beyond
                decimal to be displayed when printing
        Raises:
            ValueError if value cannot be converted to float
            ValueError if digits cannot be converted to int
        '''
        super().__init__(float(value))  # float() may raise ValueError
        self._digits = int(digits) # int() may raise ValueError

    def __add__(self, other: Number | int | float) -> Number:
        ''' method to add a Float object with any object of type
            Integer, Float, int, or float
        Parameters:
            other: an Integer or Float (i.e., Number), int, or float object
        Returns:
            a Float object 
        Raises:
            TypeError if the type of other is not one of Integer, Float,
                int, or float
        '''
        from Integer import Integer  # only when needed to avoid circular import

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Float, Integer, float, int])

        # check the type of other to determine the correct return type for add
        if isinstance(other, float) or isinstance(other, int):
            return Float(self._value + other, self._digits)  # other: no ._value
        return Float(self._value + other._value, self._digits)

    def __mul__(self, other: Number | int | float) -> Number:
        ''' method to mulitply an Integer object with any object of type
            Integer, Float, int, or float
        Parameters:
            other: an Integer, Float, int, or float object
        Returns:
            a Float object if other is of type Float or float, or
            an Integer object otherwise
        Raises:
            TypeError if the type of other is not one of Integer, Float,
                int, or float
        '''
        from Integer import Integer  # only when needed to avoid circular import

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Float, Integer, float, int])

        # check the type of other to determine the correct return type for mul
        if isinstance(other, float) or isinstance(other, int):
            return Float(self._value * other, self._digits)  # other: no ._value
        return Float(self._value * other._value, self._digits)

    def setPrecision(self, digits: int) -> None:
        ''' method to set the displayed precision of this Float object
        Parameters:
            digits: number of digits beyond the decimal to display when printed
        Raises:
            ValueError if digits cannot be converted to an int
        '''
        self._digits = int(digits)  # int may raise ValueError

    def __str__(self) -> str:
        ''' provides a string representation of this Float object
        Returns:
            a string representing the Float object, respecting the number
                of digits of precision set when the object is created or
                when later updated via setPrecision
        '''
        # use f-string formatting to display self._digits beyond the decimal
        return f"{self._value:.{self._digits}f}"

