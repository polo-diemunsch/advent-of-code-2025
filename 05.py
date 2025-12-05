from aoc import *

DAY = 5

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math

ls = s.splitlines()
si = ls.index("")
ranges = list(map(lambda x: tuple(map(int, x.split("-"))), ls[:si]))
ids = list(map(int, ls[si+1:]))


def part1():
    ans = 0

    for i in ids:
        for a, b in ranges:
            if a <= i <= b:
                ans += 1
                break

    return ans


def part2():
    ans = 0

    ranges.sort()
    a, b = ranges[0]
    for c, d in ranges[1:]:
        if c > b:
            ans += b - a + 1
            a, b = c, d
        if d > b:
            b = d

    ans += b - a + 1

    return ans


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
