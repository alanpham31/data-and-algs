def readIntegers(filename: str) -> list[int]:
    ''' this function reads integers from a file having the given filename
        and returns a list of all integers in the file
    Parameters:
        filename: the name of the file to be read
    Returns:
        a list of the integers read
    '''
    integers = []
    with open(filename, "r") as infile:
        line = infile.readline()
        while line.strip() != "":
            line_items = line.split()
            integers.extend(int(item) for item in line_items)  # Convert to integers
            line = infile.readline()

    return integers


def computeStats(integers: list[int]) -> dict[str, int]:
    ''' this function accepts a list of integers and returns a dictionary
        with four computed statistics relative to that list:  the sum,
        average, max, and min
    Parameters:
        integers: a list of integers
    Returns:
        a dictionary with four keys ('sum', 'avg', 'max', 'min') and whose
        values are the corresponding statistics as computed on the given list
    '''
    if not integers:  # Handle empty list
        return {'sum': 0, 'avg': 0, 'max': 0, 'min': 0}

    result = {'sum': 0, 'avg': 0, 'max': integers[0], 'min': integers[0]}

    for value in integers:
        result['sum'] += value
        if value > result['max']:
            result['max'] = value
        if value < result['min']:
            result['min'] = value

    result['avg'] = result['sum'] / len(integers)

    return result


def main() -> None:
    #####################################################
    # MAKE SURE TO TEST AND DEBUG EACH OF THESE FIVE
    #
    filename  = "one.txt"
    expected  = {'sum':15, 'avg':3.0, 'max':5, 'min':1}
    expected2 = None

    #filename  = "two.txt"
    #expected  = {'sum':38, 'avg':5.43, 'max':9, 'min':0}
    #expected2 = None

    #filename  = "thr.txt"
    #expected  = {'sum':0, 'avg':0, 'max':0, 'min':0}
    #expected2 = None

    #filename  = "fou.txt"
    #expected  = {'sum':1, 'avg':1.0, 'max':1, 'min':1}
    #expected2 = {'sum':6, 'avg':2.0, 'max':3, 'min':1}

    #filename  = "fiv.txt"
    #expected  = {'sum':0, 'avg':0, 'max':0, 'min':0}
    #expected2 = None
    #####################################################

    try:
        integers: list[int] = readIntegers(filename)
        results  = computeStats(integers)
    except FileNotFoundError as error:
        print(f"Error: File not found - {error}")  # Handle file not found
        return
    
    print(f"Testing with contents of {repr(filename)}:")
    print(f"   Result:   {results}")
    print(f"   Expected: {expected}", end="")
    if expected2 is not None:
        print(f" or {expected2}")
    else:
        print()

    # Compare results with expected values
    if results == expected or (expected2 is not None and results == expected2):
        print("   Test Passed!")
    else:
        print("   Test Failed!")


if __name__ == "__main__":
    main()