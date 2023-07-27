def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        operation *= -1.0
        denominator += 2.0
    return pi


def calculate_pi_lazy() -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    while True:
        pi += operation * (numerator / denominator)
        yield pi
        operation *= -1.0
        denominator += 2.0



if __name__ == "__main__":
    print(calculate_pi(150000))
    lazy = calculate_pi_lazy()
    print(calculate_pi(9999) == [next(lazy) for _ in range(9999)][-1])