from math import sqrt
def prime(n: int):
    if n < 2:
        return f"{n} isn't prime number."
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return f"{n} isn't prime number."
        i += 1
    return f'{n} is prime number.'
