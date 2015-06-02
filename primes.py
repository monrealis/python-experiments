#!/usr/bin/env python3

def isPrime(n):
    if n < 2:
        return
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def getPrimes():
    for i in range(1, 10000):
        if isPrime(i):
            yield i


n = 0
for i in getPrimes():
    print(i, end=' ')
    n += 1
    if n == 10:
        print()
        break
