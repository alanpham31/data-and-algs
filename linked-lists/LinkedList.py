from __future__ import annotations

# https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions
# Want to define our own custom Exception class...

class Node[T]:
    ''' class to implement a single node object in a singly-linked
        linked list '''
    
    __slots__ = ["data", "next"]

    def __init__(self, data: T):
        self.data: T       = data
        self.next: Node[T] = None  # can point to another Node object

class LinkedList[T]:
    ''' class to implement a singly-linked linked list '''

    def __init__(self) -> None:
        self._head: Node[T] = None   # head pointer: variable w/ addy of Node object
        self._tail: Node[T] = None   # tail pointer: variable w/ addy of Node object
        self._size: int     = 0

    def __len__(self) -> int:
        return self._size

    def appendLeft(self, item: T) -> None:
        ''' append the given T-type data item as part of a new Node to the left
            side of the linked list
        Parameters:
            item: a type T data item to be included as the data in the inserted Node
        Returns:
            nothing
        '''
        # remember to reset the tail pointer, and, when appropriate, 
        # the head pointer
        pass

    def appendRight(self, item: T) -> None:
        ''' appends the given T-type data item as part of a new Node to the right 
            of the linked list
        Parameters:
            item: a type T data item to be included as the data in the inserted Node
        Returns:
            nothing
        '''
        # remember to reset the tail pointer, and, when appropriate, 
        # the head pointer
        pass

    def popLeft(self) -> T:
        ''' removes the first Node in the linked list, returning the data item
            inside that Node
        Returns:
            a T type data item extracted from the removed Node
        Raises:
            EmptyError exception if list is empty
        '''
        # remember to handle the special case of an empty list (what should the
        # head and tail pointers be in that case?) and remember to update the
        # head & tail pointer(s) when appropriate
        pass

    def popRight(self) -> T:
        ''' removes the last Node in the linked list, returning the data item
            inside that Node
        Returns:
            a T type data item extracted from the removed Node
        Raises:
            EmptyError exception if list is empty
        '''
        # Remember to handle the special case of an empty list (what should the
        # head and tail pointers be in that case?)
        # 
        # Note: This one is trickier because you always have to walk (almost)
        # all the way through the list in order to know what the new tail
        # should be.
        #
        # Remember to update the head & tail pointer(s) when appropriate.
        pass

    def __str__(self):
        ''' returns a str representation of the linked list data
        Returns:
            an str representation of the linked list, showing head pointer
                and data tiems
        '''
        result = "head->"

        # start out at the head Node, and walk through Node by Node until we
        # reach the end of the linked list (i.e., the ._next entry is None)
        pass

        result += "<-tail"
        return result

        
def main():
    # create a LinkedList and try out some various appends and pops
    ll = LinkedList()

if __name__ == "__main__":
    main()
