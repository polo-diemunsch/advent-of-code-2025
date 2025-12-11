from aoc import *

DAY = 11

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math
import networkx as nx
from functools import cache

ls = s.splitlines()
g = {"out": []}
for l in ls:
    device, *outputs = l.split()
    device = device[:-1]
    g[device] = outputs


@cache
def dfs(current, end):
    if current == end:
        return 1

    return sum(dfs(nei, end) for nei in g[current])


def part1():
    return dfs("you", "out")


def part2():
    return dfs("svr", "fft") * dfs("fft", "dac") * dfs("dac", "out")


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
