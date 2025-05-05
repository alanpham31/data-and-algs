from code_base.Integer import Integer
import pytest

#####################################################################

# create a fixtures to represent data that will be used in tests below 

@pytest.fixture
def an_int(): return 99

@pytest.fixture
def a_float(): return 9.9

@pytest.fixture
def int_as_str(): return "88"

@pytest.fixture
def a_str(): return "xyz"

@pytest.fixture
def an_Integer(an_int): return Integer(an_int)

#####################################################################

def test_valid_Integer_object_using_int(an_int):
    print(f"Testing whether Integer({an_int}) creates valid Integer object")
    integer = Integer(an_int)
    assert(isinstance(integer, Integer))
    assert(integer._value == an_int)

def test_valid_Integer_object_using_float(a_float):
    print(f"Testing whether Integer({a_float}) creates valid Integer object")
    integer = Integer(a_float)
    assert(isinstance(integer, Integer))
    assert(integer._value == int(a_float))

def test_valid_Integer_object_using_str(int_as_str):
    print(f"Testing whether Integer({repr(int_as_str)}) creates valid Integer object")
    integer = Integer(int_as_str)
    assert(isinstance(integer, Integer))
    assert(integer._value == int(int_as_str))

def test_invalid_Integer_object_using_str(a_str):
    print(f"Testing whether Integer({repr(a_str)}) raises ValueError")
    # use pytest.raises for catching an Exception
    with pytest.raises(ValueError) as the_exception:
        integer = Integer(a_str)

def test_Integer_as_str(an_int):
    print(f"Testing __str__ on Integer object Integer({an_int})")
    integer = Integer(an_int)
    assert(integer.__str__() == str(an_int))
