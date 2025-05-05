from typing import TypeVar, Generic, List
from collections import deque
from LinkedList import LinkedList, EmptyError as LL_EmptyError

# define type var
T = TypeVar('T')

class EmptyError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)
        self.message = msg
    

class Queue(Generic[T]):
    __slots__ = ("_data")

    def __init__(self) -> None:
        # initialize empty queue
        self._data = deque()

    def push(self, ele: T) -> None:
        # add element at end of queue
        if len(self._data) > 0 and not isinstance(ele, type(self.top())):
            raise TypeError(f"cannot push {type(ele).__name__} into queue of {type(self._data.front()).__name__}")
        self._data.append(ele)

    def pop(self) -> T:
        # remove + return element at front of queue
        if len(self._data) == 0:
            raise EmptyError("queue is empty, can't pop")
        return self._data.popleft()
    
    def top(self) -> T:
        # return element at front of queue (no remove)
        if len(self._data) == 0:
            raise EmptyError("queue is empty, cant get top element")
        return self._data[0]
    
    def isEmpty(self) -> bool:
        # check if queue is empty
        return len(self._data) == 0
    
    def __len__(self) -> int:
        # return size of queue
        return len(self._data)
    
    def __str__(self) -> str:
        # return string of queue
        return str(list(self._data))
    

def main():
    # test 1 basic operations
    q = Queue[int]()
    print("new queue: ", q)
    print("is empty? ", q.isEmpty())

    # test 2 push and top
    q.push(10)
    q.push(20)
    print()
    print("after pushing 10 and 20:")
    print("queue:", q)
    print("top element:", q.top())
    print("length:", len(q))

    # test 3 pop 
    print()
    print("popped: ", q.pop())
    print("queue: ", q)
    print("popped: ", q.pop())
    print("queue: ", q)

    # test 4 edge cases
    print()
    print("testing edge cases:")
    try:
        print("pop from empty queue...")
        q.pop()
    except EmptyError as err:
        print("correctly raised: ", err)
    
    try:
        print("trying get top from empty queue...")
        q.top()
    except EmptyError as err:
        print("correctly raiased: ", err)
    
    # test 5 multiple push/pop
    print()
    print("testing multiple operations:")
    for i in range(5):
        q.push(i * 100)
    print("queue after pushes: ", q)
    while not q.isEmpty():
        print(f"popped {q.pop}, remaining length: {len(q)}")

    # test 6 same type 
    print()
    print("testing type:")
    q2 = Queue[int]()
    q2.push(1)
    try:
        q2.push("hello world")
        print("failed to catch type mismatch")
    except TypeError:
        print("correctly caught type mismatch")


if __name__ == "__main__":
    main()
