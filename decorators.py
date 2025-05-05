# decorator function that takse another function and extends behavior of latter function withouot explicitly modding it

from typing import Callable

def myfunc(func: Callable) -> None:
    func("hello world")

def main() -> None:
    myfunc(print)
    

main()