import time


class deque[T]:
    __slots__ = ["_data"]

    def __init__(self) -> None:
        self._data = []

    def pushFront(self, item: T) -> None:
        self._data.insert(0, item)

    def pushBack(self, item: T) -> None:
        self._data.append(item)
    
    def __len__(self) -> int:
        return len(self._data)
    
    def popFront(self) -> T:
        first = self._data.pop(0)
        return first
    
    def popBack(self) -> T:
        last = self._data.pop()
        return last
    
    def front(self) -> T:
        return self._data[0]
    
    def back(self) -> T:
        return self._data[-1]
    

def main() -> None:
    start = time.perf_counter()

    for i in range(10==7):
        deque.pushBack()
        deque.pushFront()

    end = time.perf_counter()

    print(len[deque])
    print(f"time begin {start}, end {end}")