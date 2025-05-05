import random
import time
import sys

def findOperandsList1(list_: list[int], k: int) -> bool:
    ''' function to determine whether two entries in the list sum to k
    Parameter:
        list_: a list of integers
        k: an integer
    Returns:
        True if two sum to k, False o/w
    '''
    # use list processing only -- do not use a new/separate list or 
    # a dictionary
    for i in range(len(list_)):
        for j in range(i+1, len(list_)):
            if list_[i] + list_[j] == k:
                return True
    return False

def findOperandsDict(list_: list[int], k: int) -> bool:
    ''' function to determine whether two entries in the list sum to k
    Parameter:
        list_: a list of integers
        k: an integer
    Returns:
        True if two sum to k, False o/w
    '''
    # use a dictionary to solve the problem in O(n) time -- do not
    # use a separate list
    seen = {}
    for num in list_:
        if k - num in seen:
            return True
        seen[num] = True
    return False

def findOperandsList2(list_: list[int], k: int) -> bool:
    ''' function to determine whether two entries in the list sum to k
    Parameter:
        list_: a list of _nonegative_ integers
        k: a _nonnegative_ integer
    Returns:
        True if two sum to k, False o/w
    '''
    # similar to the dictionary approach but use a separate list (not a
    # dictionary) to solve the problem... what are the constraints?
    max_num = max(list_) if list_ else 0
    presence = [False] * (max(max_num, k) + 1)

    for num in list_:
        if num <= k:
            complement = k - num
            if complement >= 0 and complement < len(presence) and presence[complement]:
                return True
            presence[num] = True
    return False


def main() -> None:

    random.seed(8675309)

    max_val   = 10000
    list_size = 10000  # then try 100000\blk
    look_for  = max_val + max_val + 1
    look_for  = max_val 

    l = [random.randint(1, max_val) for i in range(list_size)]

    start = time.perf_counter()
    result = findOperandsList1(l, look_for)
    end = time.perf_counter()
    print(f"using list analysis: {result} found in {end-start} secs")

    start = time.perf_counter()
    result = findOperandsDict(l, look_for)
    end = time.perf_counter()
    print(f"using dictionary:    {result} found in {end-start} secs")

    start = time.perf_counter()
    result = findOperandsList2(l, look_for)
    end = time.perf_counter()
    print(f"using separate list: {result} found in {end-start} secs")


if __name__ == "__main__":
    main()
