from typing import List, Generator


def my_sum(numbers: List[float]) -> float:
    total: float = 0
    for n in numbers:
        total += n
    return total


def infinite_stream(start: int) -> Generator:
    while True:
        yield start
        start += 1

