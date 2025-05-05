from __future__ import annotations

import copy   # for using deepcopy
import heapq
import random
import string

############################
class EmptyError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message

#################
class Entry[K,V]:
    __slots__ = ('key', 'value')

    def __init__(self, priority: K, data: V) -> None:
        self.key  : K = priority
        self.value: V = data

    def __str__(self) -> str:
        ''' returns a string representation of this key:value Entry
        Returns:
            string version of this Entry
        '''
        return f"({self.key},{self.value})"

    def __lt__(self, other: Entry[K,V]) -> bool:
        ''' determines whether this Entry is less than another Entry
        Parameters:
            other: a separate Entry object
        Returns:
            True if this's key is less than other's key, or
                if this's key and other's key are the same while
                   this's value is less than other's value
        '''
        return self.key < other.key

    # not the Pythonic way to use __repr__ but allows us to print a list of Entry
    def __repr__(self) -> str: 
        return f"({repr(self.key)},{'∅' if self.value is None else repr(self.value)})"

#######################
class PriorityQueue[K,V]:
    __slots__ = ('_container')

    def __init__(self) -> None:
        self._container: list[Entry[K,V]] = list()

    def __len__(self)  -> int:  return len(self._container)
    def isEmpty(self) -> bool:  return len(self._container) == 0

    def insert(self, key: K, item: V) -> None: 
        ''' method to create a new Entry having key (e.g., time) and
            item (e.g., event to occur at that time),  and then insert the
            Entry into the heap (self._container) using heapq.heappush
        Parameters:
            key: the entry's priority
            item: the entry's data
        '''
        entry = Entry(key, item)
        heapq.heappush(self._container, entry)

    def removeMin(self) -> Entry[K,V]:
        ''' method to remove the highest priority (e.g., minimum time) Entry
            from the PriorityQueue, returning that Entry
        Returns:
            Entry object corresponding to the highest priority Entry
        Raises:
            EmptyError if the priority queue is empty
        '''
        # remove from the heap (self._container) using heapq.heappop;
        # make sure to raise an exception when appropriate
        if self.isEmpty():
            raise EmptyError("priority queue is empty")
        return heapq.heappop(self._container)

    def min(self) -> Entry[K,V]:
        ''' method to return but not remove the highest priority (e.g., minimum
            time) Entry from the PriorityQueue, returning that Entry
        Returns:
            a copy of the Entry object corresponding to the highest priority
            Entry
        Raises:
            EmptyError if the priority queue is empty
        '''
        # return _a copy_ of the minimum event -- by returning a copy, you can 
        # make sure to not allow the user to inadvertently (or intentionally)
        # modify elements directly on the PQ in a way that could destroy the
        # necessary heap structure;
        # make sure to raise an exception when appropriate
        if self.isEmpty():
            raise EmptyError("priority queue is empty")
        return copy.deepcopy(self._container[0])

    def __str__(self) -> str:
        return str(self._container)

##########################
def main() -> None:
    pq = PriorityQueue()
    print(f"len of pq = {len(pq)}")
    # provide more tests below

    # test insertion and heap
    print()
    print("inserting items in order: 5, 3, 7, 1, 4")
    pq.insert(5, "five")
    pq.insert(3, "three")
    pq.insert(7, "seven")
    pq.insert(1, "one")
    pq.insert(4, "four")

    print(f"current heap: {pq}")
    print(f"length: {len(pq)}")

    # test min and removeMin
    print()
    print("testing min and removeMin:")
    print(f"current min: {pq.min()}")
    print(f"removed min: {pq.removeMin()}")
    print(f"current heap: {pq}")
    print(f"new min: {pq.min()}")

    # test empty queue error handling
    print()
    print("testing empty queue behavior")
    empty_pq = PriorityQueue()
    try:
        empty_pq.removeMin()
    except EmptyError as err:
        print(f"caught emptyerror: {err.message}")
    
    try:
        empty_pq.removeMin()
    except EmptyError as err:
        print(f"caught emptyerror: {err.message}")
    

if __name__ == "__main__":
    main()
