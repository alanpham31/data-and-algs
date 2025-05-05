from code_base.functions import findItem

def test_findFirstItem() -> None:
    '''
    given, when, then

    given: list of [0, 1, 2, 3, 4]: item 0
    when: user searches for 0 in list
    then: function returns true (item found)
    '''
    print("testing finditem function")
    assert(findItem([0, 1, 2, 3, 4], 0) == True)