def sum_multiples_3_5(n: int) -> int:
    """
    Returns the sum of all multiples of 3 or 5 below n.
    """
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

print(sum_multiples_3_5(1000))
