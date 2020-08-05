from itertools import takewhile
import itertools

def primes(n=2):
    while (True):
        for x in range(2, n):
            if n % x == 0:
                break
                # если делителей нет, добавляем число в список
        else: yield n
        n += 1

print(list(itertools.takewhile(lambda x : x <= 31, primes())))