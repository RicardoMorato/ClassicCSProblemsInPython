from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional, Protocol
from heapq import heappush, heappop

C = TypeVar('C', bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        return super().__eq__(other)

    def __lt__(self: C, other: C) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other

def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high = len(sequence) - 1

    while low <= high:
        mid: int = (low + high) // 2

        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True

    return False

if __name__ == "__main__":
    print(binary_contains(["a", "d", "e", "f", "z"], "f"))
    print(binary_contains(["John", "Mark", "Ronald", "Sarah", "Zidane"], "François"))
