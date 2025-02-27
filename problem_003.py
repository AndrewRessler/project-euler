from sympy import isprime, primefactors

def find_largest_prime_factor(n: int) -> int:
    """
    Returns the largest prime factor of n.
    """
    remaining_n = n
    largest_prime = None

    for i in range(2, int(n**0.5) + 1):
        if isprime(i):
            while remaining_n % i == 0:
                largest_prime = i
                remaining_n //= i

        if remaining_n == 1:
            break

    # If remaining_n > 1, it must be prime (this catches cases where n itself is prime)
    return max(largest_prime, remaining_n) if largest_prime else n

print(find_largest_prime_factor(600851475143))
