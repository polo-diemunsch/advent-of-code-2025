from aoc import *

DAY = 6

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math
import operator
from functools import reduce

ls = s.splitlines()
pbs = [list(map(int, l.split())) for l in ls[:-1]]
ops = [operator.add if op == "+" else operator.mul for op in ls[-1].split()]

ops2 = []
op = ls[-1][0]
i = 0
for l in ls[-1][1:]:
    if l != " ":
        ops2.append((operator.add if op == "+" else operator.mul, i))
        op = l
        i = 0
    else:
        i += 1
ops2.append((operator.add if op == "+" else operator.mul, i + 1))


def part1():
    ans = 0

    for i in range(len(ops)):
        ans += reduce(ops[i], [pb[i] for pb in pbs])

    return ans


def part2():
    ans = 0

    i = 0
    for op, ds in ops2:
        nbs = [""] * ds

        for j in range(len(pbs)):
            for k in range(len(nbs)):
                nbs[k] += ls[j][i+k]

        ans += reduce(op, map(int, nbs))

        i += ds + 1

    return ans


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
