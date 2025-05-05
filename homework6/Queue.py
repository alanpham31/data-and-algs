from typing import TypeVar, Generic, List

# define type var
T = TypeVar("T")

class EmptyError(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)
        self.message = msg
    

class Queue(Generic[T]):
    __slots__ = ("_data")

    def __init__(self) -> None:
        # initialize empty queue
        self._data: List[T] = []

    def push(self, ele: T) -> None:
        # add element at end of queue
        self._data.append(ele)

    def pop(self) -> T:
        # remove + return element at front of queue
        if self.isEmpty():
            raise EmptyError("queue is empty, cant pop")
        return self._data.pop(0)
    
    def top(self) -> T:
        # return element at front of queue (no remove)
        if self.isEmpty():
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
        return str(self._data)
    

def main():
    q: Queue[int] = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(f"Queue: {q}")
    print(f"Top element: {q.top()}")
    print(f"Popped element: {q.pop()}")
    print(f"Queue after pop: {q}")
    print(f"Is queue empty? {q.isEmpty()}")
    print(f"Queue length: {len(q)}")


if __name__ == "__main__":
    main()
