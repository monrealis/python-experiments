#!/usr/bin/env python3

def print_first_ten_primes():
    n = 0
    for i in get_primes():
        print(i, end=' ')
        n += 1
        if n == 10:
            print()
            break

def get_primes():
    for i in range(1, 10000):
        if is_prime(i):
            yield i

def is_prime(n):
    if n < 2:
        return
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__': print_first_ten_primes()
