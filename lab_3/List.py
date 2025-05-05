import ctypes

# for generic type T, see
# https://docs.python.org/3/whatsnew/3.12.html#pep-695-type-parameter-syntax
class List[T]:
    __slots__ = ('_array',              # reference to the ctypes array
                 '_num_user_items',     # current number of user's items in the List
                 '_capacity',           # total length of the ctypes array
                 '_num_resizes',        # number of array resizes performed
                 '_num_copies_append',  # number of item-to-item copies req'd on appending
                 '_num_copies_remove')  # number of item-to-item copies req'd on removing

    def __init__(self):
        ''' initializer for a List class object, which allocates space for
            a length-1 initally empty underlying array '''
        self._num_user_items = 0  # number of user items currently in the List
        self._capacity       = 1  # default List capacity at startup is 1

        self._array          = self._makeArray(self._capacity)

        # for internal stats (see comments above)
        self._num_resizes = 0
        self._num_copies_append = 0
        self._num_copies_remove = 0

    def getInternalStats(self) -> dict:
        ''' method to return a dictionary containing information about the
            resizing-related statistics
        Returns:
            a dictionary with:
                current List capacity
                total number of resizes performed
                total number of item-to-item copies resulting from an append
                total number of item-to-item copies resulting from a remove
        '''
        return {"capacity"      : self._capacity, \
                "resizes"       : self._num_resizes, \
                "append_copies" : self._num_copies_append, \
                "remove_copies" : self._num_copies_remove}

    def _makeArray(self, capacity: int) -> ctypes.Array:
        ''' private method to reserve space for a low-level array of a
            given capacity
        Parameters:
            capacity: integer size of the array to be created
        Returns:
            a ctypes low-level array whose size is the given capacity
        '''
        ArrayType = (capacity * ctypes.py_object)  # py_object defined in ctypes
        return ArrayType() # create and return an array of py_object of size capacity

    def __len__(self) -> int:
        ''' returns number of user items currently stored in the List
        Returns:
            integer count of number of user items
        '''
        return self._num_user_items

    def __getitem__(self, index: int) -> T:
        ''' returns the item in the List at the given index
        Parameters:
            index: integer index between 0 and length - 1
        Returns:
            item of type T at the given index
        Raises:
            IndexError exception if index is invalid (i.e., negative or
                >= the number of user items in the List)
        '''
        if not 0 <= index < self._num_user_items:
            raise IndexError("index out of range")
        return self._array[index]

    def __setitem__(self, index: int, new_item: T) -> None:
        if not 0 <= index < self._num_user_items:
            raise IndexError("index out of range")
        self._array[index] = new_item

    def append(self, new_item: T) -> None:
        ''' appends the given item to the List
        Parameters:
            new_item: type-T item to append to the List
        Returns:
            Nothing
        Raises:
            TypeError exception if type of item does not match types already
                present in the List (first appended item determines List type)
        '''
        # also remember to raise an exception when approriate

        # check whether array is full, and if so, allocate more space
        if self._num_user_items == self._capacity:
            new_capacity = int(self._capacity * 2^15)  # resize factor
            if new_capacity <= self._capacity:  # capacity increases
                new_capacity = self._capacity + 1
            self._resizeArray(new_capacity)
        # add the item to the array and increment the number of user items
        self._array[self._num_user_items] = new_item
        self._num_user_items += 1

    def remove(self, item: T) -> None:
        ''' removes the first occurrence of item in the List
        Parameters:
            item: type-T element to remove from the List
        Returns:
            Nothing
        Raises:
            ValueError exception if given item does not exist in the List
        '''
        for i in range(self._num_user_items):
            if self._array[i] == item:
                self._removeAtIndex(i)
                return
        raise ValueError("item not found in list")
    
    def _removeAtIndex(self, index: int) -> None:
        if not 0 <= index < self._num_user_items:
            raise IndexError("index out of range")
        for i in range(index, self._num_user_items - 1):
            self._array[i] = self._array[i + 1]
            self._num_copies_remove += 1
        self._num_user_items -= 1

    def _resizeArray(self, new_capacity: int) -> None:
        ''' private method to resize the underlying array to a specific
            capacity, copying elements from the old array into the new
        Parameters:
            new_capacity: integer size of the new array
        Returns:
            Nothing
        '''
        # use private _makeArray method to make a new array;
        # then copy over the old data from existing array into new array;
        # then make sure to update the _array and _capacity instance variables
        new_array = self._makeArray(new_capacity)
        for i in range(self._num_user_items):
            new_array[i] = self._array[i]
            self._num_copies_append += 1
        self._array = new_array
        self._capacity = new_capacity
        self._num_resizes += 1

    def __str__(self) -> str:
        ''' a string representation of this List
        Returns:
            a printable string format of the List contents
        '''
        result = "["
        for i in range(self._num_user_items):
            result += str(self._array[i]) + ","
        # remove any trailing comma (for non-empty lLsts only)
        if self._num_user_items != 0: result = result[:-1]
        result += "]"
        return result


def main() -> None:
    # your tests will go below
    #l = List()
    l = List[int]()
    for i in range(10):
        l.append(i)
    print(l)
    l.remove(5)
    print(l)
    print(l.getInternalStats())

if __name__ == "__main__":
    main()
