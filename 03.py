from aoc import *

DAY = 3

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math

ls = s.splitlines()


def part1():
    ans = 0

    for l in ls:
        a, b = map(int, l[-2:])
        for c in map(int, l[-3::-1]):
            if c >= a:
                if a > b:
                    b = a
                a = c
        ans += a * 10 + b

    return ans


def part2():
    ans = 0

    for l in ls:
        p = list(map(int, l[-12:]))
        for c in map(int, l[-13::-1]):
            tmp = c
            for i in range(len(p)):
                if tmp >= p[i]:
                    p[i], tmp = tmp, p[i]
                else:
                    break
        ans += int("".join(map(str, p)))

    return ans


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
