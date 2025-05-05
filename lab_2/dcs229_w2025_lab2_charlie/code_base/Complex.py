from code_base.Number import Number

class Complex(Number):
    def __init__(self, real, imag):
        """Initializes a Complex number with real and imaginary parts."""
        super().__init__(real)  # Calls the parent class constructor for real part
        self.real = real
        self.imag = imag  # Stores the imaginary part
        self.precision = 1  # Default precision for formatting

    def __add__(self, other):
        """Defines addition for Complex numbers and compatible numeric types."""
        if isinstance(other, Complex):  
            new_real = self.real + other.real
            new_imag = self.imag + other.imag
            return Complex(new_real, new_imag)
        
        elif isinstance(other, (int, float)):  
            return Complex(self.real + other, self.imag)

        elif isinstance(other, Number):  
            return Complex(self.real + other.real, self.imag)

        return NotImplemented  

    def __mul__(self, other):
        """Defines multiplication for Complex numbers and compatible numeric types."""
        if isinstance(other, Complex):  
            new_real = (self.real * other.real) - (self.imag * other.imag)
            new_imag = (self.real * other.imag) + (self.imag * other.real)
            return Complex(new_real, new_imag)

        elif isinstance(other, (int, float)):  
            return Complex(self.real * other, self.imag * other)

        elif isinstance(other, Number):  
            return Complex(self.real * other.real, self.imag * other.real)

        else:
            raise TypeError("Unsupported operand type")
        return NotImplemented


    def setPrecision(self, precision):
        self.precision = precision

    def __str__(self):
        real_part = f"{self.real}" if self.real != 0 else ""
        imag_part = ""

        if self.imag != 0:
            if self.imag == 1: # special case fix for plus or minus 1
                imag_str = ""
            elif self.imag == -1:
                imag_str = "-"
            else:
                imag_str = f"{abs(self.imag):.{self.precision}f}" if isinstance(self.imag, float) else str(abs(self.imag))
            
            imag_part = f"{imag_str}i"
            if self.imag > 0 and self.real != 0:
                imag_part = " + " + imag_part
            elif self.imag < 0 and self.imag != -1:
                imag_part = " - " + imag_part

        return real_part + imag_part if real_part or imag_part else "0"
