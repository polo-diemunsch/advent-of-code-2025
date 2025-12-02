from aoc import *

DAY = 2

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math

ls = s.splitlines()


def part1():
    ans = 0

    for l in ls:
        for a, b in map(lambda x:map(int, x.split("-")), l.split(",")):
            for i in range(a, b + 1):
                j = str(i)
                if j[:len(j)//2] == j[len(j)//2:]:
                    ans += i

    return ans


def part2():
    ans = 0

    for l in ls:
        for a, b in map(lambda x:map(int, x.split("-")), l.split(",")):
            for i in range(a, b + 1):
                j = str(i)
                for k in range(1, len(j) // 2 + 1):
                    invalid = True
                    for l in range(k, len(j), k):
                        if j[l-k:l] != j[l:l+k]:
                            invalid = False
                            break
                    if invalid:
                        ans += i
                        break

    return ans


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
