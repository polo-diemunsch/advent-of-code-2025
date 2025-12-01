from aoc import *

DAY = 1

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math

ls = s.splitlines()


def part1():
    ans = 0

    d = 50
    for l in ls:
        nb = int(l[1:])
        f = -1 if l[0] == "L" else 1
        d = (d + f * nb) % 100
        if d == 0:
            ans += 1

    return ans


def part2():
    ans = 0

    d = 50
    for l in ls:
        nb = int(l[1:])
        f = -1 if l[0] == "L" else 1
        ld = d
        d += f * nb
        ans += abs((ld - ld % 100) - (d - d % 100)) // 100
        if l[0] == "L":
            if ld % 100 == 0:
                ans -= 1
            elif d % 100 == 0:
                ans += 1

    return ans


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
