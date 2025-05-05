from __future__ import annotations
from abc import ABC, abstractmethod
from inspect import stack as inspect_stack

######################################################################
class Number(ABC):  # an abstract base class
    __slots__ = ('_value')

    def __init__(self, value: int | float):
        self._value = value

    @abstractmethod
    def __add__(self, other: Float | Integer) -> Float | Integer:
        ''' adds two Number objects, returning the Number result as
            either an Integer or Float appropriately
        Parameters:
            other: a different Integer or Float object
        Returns:
            an Integer or Float object representing the sum
        '''
        pass  # subclasses must handle the implementation

    @abstractmethod
    def __mul__(self, other: Float | Integer) -> Float | Integer:
        ''' multiplies two Number objects, returning the Number result as
            either a Integer or Float appropriately
        Parameters:
            other: a different Integer or Float object
        Returns:
            an Integer or Float object representing the product
        '''
        pass  # subclasses must handle the implementation

    def __str__(self) -> str:
        ''' returns a string representation of this Number object
        Returns:
            a string representing the Number object
        '''
        return f"{self._value}"

    def checkType(self, other: Number | int | float, types: list[type] = None) -> None:
        ''' checks the type of other object for a given operation, raising
            an exception if not among a specified list of types (defaulting to
            Number)
        Parameters:
            other: expecting an object of type Number, int, or float
        Raises:
            TypeError if other is not among the specified list of types
        '''
        if types is None:
            types = [Number]  # default to check for type Number only

        # look for any is-a match of provided types
        found = any(isinstance(other, type_) for type_ in types)

        if not found:
            # get the class name and function name of the calling method
            # (see https://docs.python.org/3/library/inspect.html#inspect.stack)
            caller_info = inspect_stack()[1]
            class_name  = caller_info.frame.f_locals['self'].__class__.__name__
            fcn_name    = caller_info.function
            msg = f"invalid operand type {type(other).__name__} for " + \
                  f"{class_name}.{fcn_name}"
            raise TypeError(msg)

