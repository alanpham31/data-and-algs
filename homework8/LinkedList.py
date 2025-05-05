from __future__ import annotations

######################################################################
class EmptyError(Exception):
    ''' class to represent an empty list exception '''
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

######################################################################
class Node[T]:
    ''' class to represent a node in a doubly-linked list '''
    def __init__(self, data: T):
        self.data: T      = data
        self.prev: Node[T] = None  # pointer to the previous Node in the list
        self.next: Node[T] = None  # pointer to the next Node in the list

######################################################################
class LinkedList[T]:
    ''' class to implement a doubly-linked list '''
    __slots__ = ('_head', '_tail', '_size')

    def __init__(self) -> None:
        self._head: Node[T] = None   # head pointer: contains addy of one Node object
        self._tail: Node[T] = None   # tail pointer: contains addy of one Node object
        self._size: int     = 0      # number of entries in the list

    def __len__(self) -> int:
        ''' returns the number of entries in the linked list
        Returns:
            integer valued number of list entries
        '''
        return self._size

    def front(self) -> T:
        ''' method to return the data item at the front of the list without
            removing that node
        Returns:
            the T-valued item at the front of the list
        Raises:
            EmptyError if the list is empty
        '''
        if self._head is None:
            raise EmptyError("list is empty")
        return self._head.data

    def back(self) -> T:
        ''' method to return the data item at the end of the list without
            removing that node
        Returns:
            the T-valued item at the end of the list
        Raises:
            EmptyError if the list is empty
        '''
        if self._tail is None:
            raise EmptyError("list is emtpy")
        return self._tail.data

    def appendLeft(self, item: T) -> None:
        ''' adds the given T-type data item as part of a new Node to the left
            of the linked list
        Parameters:
            item: a type T data item to be included as the data in the inserted Node
        Raises:
            TypeError if non-empty list and item type does not match list entry types
        '''
        if self._size > 0 and isinstance(item, type(self._head.data)):
            raise TypeError("item type does not match list entry types")
        new_node = Node(item)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        self._size += 1

    def appendRight(self, item: T) -> None:
        ''' adds the given T-type data item as part of a new Node to the right 
            of the linked list
        Parameters:
            item: a type T data item to be included as the data in the inserted Node
        Raises:
            TypeError if non-empty list and item type does not match list entry types
        '''
        if self._size > 0 and not isinstance(item, type(self._head.data)):
            raise TypeError("item type does not match list entry types")
        new_node = Node(item)
        if self._tail is None:
            self._head = self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def popLeft(self) -> T:
        ''' removes the first Node in the linked list, returning the data item
            inside that Node
        Returns:
            a T type data item extracted from the removed Node
        Raises:
            EmptyError exception if list is empty
        '''
        if self._head is None:
            raise EmptyError("list is empty")
        data = self._head.data
        if self._head.next is None:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return data

    def popRight(self) -> T:
        ''' removes the last Node in the linked list, returning the data item
            inside that Node
        Returns:
            a T type data item extracted from the removed Node
        Raises:
            EmptyError exception if list is empty
        '''
        if self._tail is None:
            raise EmptyError("list is empty")
        data = self._tail.data
        if self._tail.prev is None:
            self._head = self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        self._size -= 1
        return data

    def __str__(self):
        ''' a str representation of the linked list data
        Returns:
            str representation of the linked list, showing head and tail
            pointers and list data items
        '''
        str_ = "head->"
        # start out at the head Node, and walk through Node by Node until we
        # reach the end of the linked list (i.e., the ._next entry is None)
        ptr_ = self._head
        while ptr_ is not None:
            str_ += "[" + repr(ptr_.data) + "]<->"   # use of repr will print quotes with strings
            ptr_ = ptr_.next  # move ptr_ to the next Node in the linked list

        if self._head != None: str_ = str_[:-3]  # remove the last "<->"
        str_ += "<-tail"
        return str_
        
###################
def main() -> None:
    # create a LinkedList and try out some various adds and removes
    ll = LinkedList()

    # your tests here...

    # did you test:
    #   popLeft from an empty list?
    #   popRight from an empty list?
    #   popping the leftmost element from a non-empty list?
    #   poping the rightmost element from a non-empty list?
    #   appending to the right of an empty list?
    #   appendRight to an empty list, immediately followed by appendLeft?
    #   appending to the right of a non-empty list?
    #   appending to the left of an empty list?
    #   appendLeft to an empty list, immediately followed by appendRight?
    #   appending to the left of a non-empty list?
    #   various exceptions as appropriate?

    # make linkedlist
    ll = LinkedList()
    
    # test appending right
    ll.appendRight(1)
    print(ll)

    # test append left - not empty list
    ll.appendLeft(0)
    print(ll)

    # test append right - not empty list
    ll.appendRight(19)
    print(ll)

    # test pop left
    print(ll.popLeft())
    print(ll)

    # test pop right
    print(ll.popRight())
    print(ll)

    # test pop last element
    print(ll.popLeft())
    print(ll)

    # test pop empty list - EmptyError
    try:
        ll.popLeft()
    except EmptyError as err:
        print(err)

    # test append left of empty list
    ll.appendLeft(22)
    print(ll)

    # test apeend right of empty list
    ll.appendRight(420)

    # test pop farest right element from non-empty list
    print(ll.popRight())
    print(ll)

    # test pop farest left element from non-empty list
    print(ll.popLeft())
    print(ll)

    # test append left of empty list followed appendRight
    ll.appendLeft(100)
    ll.appendRight(200)
    print(ll)

    # test append right of empty list followed appendLeft
    ll = LinkedList()
    ll.appendRight(200)
    ll.appendLeft(100)

    # test TypeError appending mismatched types
    try:
        ll.appendLeft("hello wowlrd")
    except TypeError as err:
        print(err)


    ll.front()
    ll.back()

    ll.appendLeft(1)
    ll.appendLeft(2)
    ll.appendLeft(3)
    ll.appendLeft(4)
    ll.popRight()
    ll.popRight()
    ll.popRight()
    ll.popRight()

    ll.front()
    ll.back()
    

if __name__ == "__main__":
    main()
