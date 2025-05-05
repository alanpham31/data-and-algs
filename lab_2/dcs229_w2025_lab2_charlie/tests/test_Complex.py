import pytest
from code_base.Complex import Complex

@pytest.fixture
def complex_numbers():
    return [
        (Complex(3, 4), 3, 4),
        (Complex(0, 0), 0, 0),
        (Complex(-2, 5), -2, 5),
        (Complex(1.5, -3.2), 1.5, -3.2)
    ]

def test_complex_init(complex_numbers):
    for complex_num, expected_real, expected_imag in complex_numbers:
        assert complex_num.real == expected_real, f"Expected real: {expected_real}, got {complex_num.real}"
        assert complex_num.imag == expected_imag, f"Expected imag: {expected_imag}, got {complex_num.imag}"
        assert complex_num.precision == 1, f"Expected default precision: 1, got {complex_num.precision}"

def test_set_precision(complex_numbers):
    complex_num, _, _ = complex_numbers[0]
    complex_num.setPrecision(3)
    assert complex_num.precision == 3, f"Expected precision: 3, got {complex_num.precision}"

def test_str_representation():
    assert str(Complex(3, 4)) == "3 + 4i"
    assert str(Complex(0, 1)) == "i"
    assert str(Complex(0, -1)) == "-i"
    assert str(Complex(0, 0)) == "0"
    assert str(Complex(3.1, 2)) == "3.1 + 2i"
    assert str(Complex(-3, -2.1)) == "-3 - 2.1i"

def test_add():
    c1 = Complex(3, 4)
    c2 = Complex(1, -2)
    result = c1 + c2
    assert result.real == 4 and result.imag == 2, f"Expected (4,2), got ({result.real},{result.imag})"

def test_mul():
    c1 = Complex(3, 4)
    c2 = Complex(1, -2)
    result = c1 * c2
    assert result.real == 11 and result.imag == -2, f"Expected (11,-2), got ({result.real},{result.imag})"

    scalar_result = c1 * 2
    assert scalar_result.real == 6 and scalar_result.imag == 8, f"Expected (6,8), got ({scalar_result.real},{scalar_result.imag})"

def test_add_int():
    c = Complex(3, 4)
    i = 5
    result = c + i
    assert result.real == 8 and result.imag == 4, f"Expected (8, 4) got ({result.real}, {result.imag})"

def test_add_float():
    c = Complex(3, 4)
    f = 2.5
    result = c + f
    assert result.real == 5.5 and result.imag == 4, f"Expected (5.5,4), got ({result.real},{result.imag})"

def test_str_edge_cases():
    assert str(Complex(0, 0)) == "0", "Expected '0' for (0, 0)"
    assert str(Complex(0, 1)) == "i", "Expected 'i' for (0, 1)"
    assert str(Complex(0, -1)) == "-i", "Expected '-i' for (0, -1)"
    assert str(Complex(1, 0)) == "1", "Expected '1' for (1, 0)"
    assert str(Complex(-1, 0)) == "-1", "Expected '-1' for (-1, 0)"
    assert str(Complex(0, 2)) == "2i", "Expected '2i' for (0, 2)"

def test_add_invalid_type():
    c = Complex(3, 4)
    with pytest.raises(TypeError):
        result = c + "invalid"  # Adding a string should raise TypeError

def test_mul_invalid_type():
    c = Complex(3, 4)
    with pytest.raises(TypeError):
        result = c * "invalid"  # Multiplying by a string should raise TypeError