from typing import Iterable, TypeVar

T = TypeVar("T")

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True

    return False

if __name__ == "__main__":
    print(linear_contains([1, 5, 15, 15, 15, 20], 5))
    print(linear_contains(["Hulk", "Thor", "Black Widow", "Black Panther", "Iron Man", "Capitan America"], "Vision"))
