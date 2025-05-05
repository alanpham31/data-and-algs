from Number import Number

######################################################################
class Integer(Number):
    def __init__(self, value: int) -> None:
        ''' initializer method for Integer class
        Parameter:
            value: an integer
        Raises:
            ValueError if value cannot be converted to int
        '''
        super().__init__(int(value))

    def __add__(self, other: Number | int | float) -> Number:
        ''' method to add an Integer object with any object of type
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
        from Float import Float  # only when needed to avoid circular import

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float])

        # check the type of other to determine the correct return type for add
        if isinstance(other, Float):
            return Float(self._value + other._value)
        if isinstance(other, float):
            return Float(self._value + other)
        if isinstance(other, int):
            return Integer(self._value + other)
        return Integer(self._value + other._value)

    def __mul__(self, other: Number) -> Number:
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
        from Float import Float  # only when needed to avoid circular import

        # call Number's checkType helper to raise an exception when appropriate
        self.checkType(other, [Integer, Float, int, float])

        # check the type of other to determine the correct return type for mul
        if isinstance(other, Float):
            return Float(self._value * other._value)
        if isinstance(other, float):
            return Float(self._value * other)
        if isinstance(other, int):
            return Integer(self._value * other)
        return Integer(self._value * other._value)


