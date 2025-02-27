def sum_even_fibonacci(n: int) -> int:
    """
    Returns the sum of even Fibonacci numbers not exceeding n.
    """
    total_sum = 0
    num_1, num_2 = 0, 1

    while num_2 <= n:
        if num_2 % 2 == 0:
            total_sum += num_2
        num_1, num_2 = num_2, num_1 + num_2

    return total_sum

print(sum_even_fibonacci(4000000))
