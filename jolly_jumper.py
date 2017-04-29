#!/usr/bin/env python3

import itertools

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def is_jolly(numbers):
    n = numbers[0]
    rest = numbers[1:]

    expected_sum = (n - 1) * ((1 + (n - 1)) // 2)
    actual_sum = 0

    for x, y in pairwise(rest):
        actual_sum = actual_sum + abs(x - y)

    if actual_sum == expected_sum:
        return True
    else:
        return False

if __name__ == '__main__':
    print(is_jolly([4, 1, 4, 2, 3]))
    print(is_jolly([5, 1, 4, 2, -1, 6]))
    print(is_jolly([4, 19, 22, 24, 21]))
    print(is_jolly([4, 19, 22, 24, 25]))
    print(is_jolly([4, 2, -1, 0, 2]))
