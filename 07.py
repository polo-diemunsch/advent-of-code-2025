from aoc import *

DAY = 7

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math

ls = s.splitlines()


def part1():
    ans = 0

    beams = {ls[0].find("S")}
    for i in range(1, len(ls)):
        new_beams = beams.copy()
        for j in beams:
            if ls[i][j] == "^":
                ans += 1
                new_beams.remove(j)
                new_beams.add(j - 1)
                new_beams.add(j + 1)
        beams = new_beams

    return ans


def part2():
    beams = {ls[0].find("S"): 1}
    for i in range(1, len(ls)):
        new_beams = beams.copy()
        for j in beams:
            if ls[i][j] == "^":
                c = new_beams.pop(j)
                new_beams[j - 1] = new_beams.get(j - 1, 0) + c
                new_beams[j + 1] = new_beams.get(j + 1, 0) + c
        beams = new_beams

    return sum(beams.values())


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
