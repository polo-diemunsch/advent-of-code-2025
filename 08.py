from aoc import *

DAY = 8

s = get_input(DAY)
# s = get_example(DAY)

import math
import collections
import operator
from functools import reduce

ls = s.splitlines()
vertices = [tuple(map(int, l.split(","))) for l in ls]
edges = []
for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        edges.append((math.dist(vertices[i], vertices[j]), i, j))
edges.sort()


class UnionFind:
    """An implementation of a Union-Find data structure for hashable types.
       All the elements are given at the start and this class supports only
       the union and find operations, as well as checking if two elements
       belong to the same set.
       These 3 operations have a time complexity O(a(n)), where a is the
       inverse Ackermann function, such that a(n) < 5 for any n that can be
       written in this physical universe.
    """

    def __init__(self, singletons):
        """Initialize the data structure with the elements of the given
           iterable as singletons.
        """
        self.parents = {e: e for e in singletons}
        self.size = {e: 1 for e in singletons}
        self.last_connection = (-1, -1)

    def find(self, e):
        """Return the root of the tree containing the given element, or None
           if the element cannot be found. Applies path compression.
        """
        if e not in self.parents:
            return None
        if self.parents[e] != e:
            self.parents[e] = self.find(self.parents[e])
        return self.parents[e]

    def union(self, e1, e2):
        """Merge the sets containing the elements e1 and e2, by rank.
        """
        r1, r2 = self.find(e1), self.find(e2)
        if r1 == r2:  # The elements are already in the same set
            return
        # We choose that r1 will be the root with the lowest size
        if self.size[r1] < self.size[r2]:
            r1, r2 = r2, r1
        # We choose r1 as the parent of r2 and update r1's rank
        self.parents[r2] = r1
        self.size[r1] += self.size[r2]
        self.last_connection = (e1, e2)

    def is_same_set(self, e1, e2):
        """Determines whether e1 and e2 are in the same set.
        """
        return self.find(e1) == self.find(e2)


def part1():
    uf = UnionFind(list(range(len(vertices))))
    for _, i, j in edges[:1000]:
        uf.union(i, j)

    group_sizes = []
    for e, p in uf.parents.items():
        if e == p:
            group_sizes.append(uf.size[e])
    group_sizes.sort(reverse=True)

    return reduce(operator.mul, group_sizes[:3])


def part2():
    uf = UnionFind(list(range(len(vertices))))
    for _, i, j in edges:
        uf.union(i, j)

    i, j = uf.last_connection

    return vertices[i][0] * vertices[j][0]


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
