import numpy as np
from typing import Generator
from time import time


def fibonacci_matrix(n):
    base_matrix = np.array([[1, 1], [1, 0]], dtype=object)  # the base_matrix [[1,1], [1,0]] represents the recurrence relation of the fibonacci sequence
    result_matrix = np.linalg.matrix_power(base_matrix, n)  # matrix to the power of n
    return result_matrix[0, 1] # second column of the first line represents the n-th number of the sequence


def fib(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, next + last
        yield next


if __name__ == "__main__":
    start1 = time()
    fibonacci_matrix(100000)
    elapsed1 = time() - start1
    start2 = time()
    [x for x in fib(100000)]
    elapsed2 = time() - start2

    print(f'{elapsed1} <> {elapsed2}')


