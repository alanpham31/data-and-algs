class EmptyError(Exception):
    def __init__(self, msg: str) -> None:
        self.message = msg

class Stack[T]:

    __slots__ = ("_data")

    def __init__(self) -> None:
        self._data: list[T] = [] # nothing in stack

    def __len__(self) -> int:
        return len(self._data)
    
    def push(self, element: T) -> None:
        self._data.append(element) # check element is the same data type as the rest of stack

    def pop(self) -> T:
        if len(self._data == 0):
            raise EmptyError("cant pop empty stack")
        return self._data.pop() # calling list class's pop

    def __str__(self) -> str:
        result = "__ top __\n"
        for i in range(len(self._data) - 1, -1, -1):
            result += str(self._data[i]) + "\n"
        result += "__ bot __\n"
    
def main() -> None:
    s = Stack()
    print(f"length: {len(s)}")

    s.push(1)
    s.push(3)
    s.push(10)
    print(s)

if __name__ == "__main__":
    main()