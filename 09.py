from aoc import *

DAY = 9

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math

ls = s.splitlines()
tiles = [tuple(map(int, l.split(","))) for l in ls]
n = len(tiles)


def part1():
    ans = 0

    for i in range(n):
        a, b = tiles[i]
        for j in range(i + 1, n):
            c, d = tiles[j]
            area = (abs(a - c) + 1) * (abs(b - d) + 1)
            if area > ans:
                ans = area

    return ans


def part2():
    ans = 0

    horizontal = []
    vertical = []
    for i in range(n):
        q1 = tiles[i]
        q2 = tiles[(i + 1) % n]
        is_hor = q1[0] == q2[0]
        li = horizontal if is_hor else vertical
        li.append((q1, q2))


    def intersects(x, y, z, i, j, k):
        return min(x, y) <= z <= max(x, y) and min(i, j) <= k <= max(i, j)


    def is_crossing(p1, p2):
        is_hor = p1[0] == p2[0]
        li = vertical if is_hor else horizontal
        for q1, q2 in li:
            if is_hor:
                if intersects(q1[0], q2[0], p1[0], p1[1], p2[1], q1[1]):
                    return True
            else:
                if intersects(p1[0], p2[0], q1[0], q1[1], q2[1], p1[1]):
                    return True

        return False


    for i in range(n):
        a, b = tiles[i]
        for j in range(i + 1, n):
            c, d = tiles[j]

            area = (abs(a - c) + 1) * (abs(b - d) + 1)
            if area < ans:
                continue

            s1, s2 = sgn(c - a), sgn(d - b)
            lines = [
                ((a + s1, b + s2), (a + s1, d - s2)),
                ((a + s1, d - s2), (c - s1, d - s2)),
                ((c - s1, d - s2), (c - s1, b + s2)),
                ((c - s1, b + s2), (a + s1, b + s2)),
            ]
            if any(is_crossing(e, f) for e, f in lines):
                continue

            ans = area

    return ans


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
