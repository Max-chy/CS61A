def square(x):
    print("here!")
    return x * x
def so_slow(num):
    x = num
    x = x + 1
    return x / 1

square(so_slow(5))

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    m = n - 1
    while m > 1:
        if n % m == 0:
            return False
        m -= 1
    return True