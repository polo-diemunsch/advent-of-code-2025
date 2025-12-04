from aoc import *

DAY = 4

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math

ls = [list(l) for l in s.splitlines()]


def part1():
    ans = 0

    for i in range(len(ls)):
        for j in range(len(ls[i])):
            count = 0
            if ls[i][j] != "@":
                continue
            for di, dj in DIR8:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(ls) and 0 <= nj < len(ls[i]) and ls[ni][nj] == "@":
                    count += 1
            if count < 4:
                ans += 1

    return ans


def part2():
    ans = 0

    removed = True
    while removed:
        removed = False
        for i in range(len(ls)):
            for j in range(len(ls[i])):
                count = 0
                if ls[i][j] != "@":
                    continue
                for di, dj in DIR8:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(ls) and 0 <= nj < len(ls[i]) and ls[ni][nj] == "@":
                        count += 1
                if count < 4:
                    ans += 1
                    ls[i][j] = "."
                    removed = True

    return ans


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
