from aoc import *

DAY = 10

s = get_input(DAY)
# s = get_example(DAY)

import collections
import math
from ortools.linear_solver import pywraplp

ls = s.splitlines()


def part1():
    ans = 0


    def bfs(start, end, edges):
        q = [start]
        visited = {start}

        count = 0
        while len(q) > 0:
            new_q = []
            for current in q:
                if current == end:
                    return count
                for edge in edges:
                    nei = current ^ edge
                    if nei not in visited:
                        new_q.append(nei)
                        visited.add(nei)
            q = new_q
            count += 1

        return -1


    for l in ls:
        lights, *buttons, _joltages = l.split()
        target = sum(2**i if e == "#" else 0 for i, e in enumerate(lights[1:-1]))
        edges = [sum(2**e for e in map(int, button[1:-1].split(","))) for button in buttons]

        ans += bfs(0, target, edges)

    return ans


def part2():
    ans = 0

    for l in ls:
        _lights, *buttons, joltages = l.split()
        target = list(map(int, joltages[1:-1].split(",")))
        edges = [[0] * len(buttons) for _ in range(len(target))]

        solver = pywraplp.Solver.CreateSolver("CBC")
        variables = []

        for i, button in enumerate(buttons):
            m = 0
            for l in map(int, button[1:-1].split(",")):
                edges[l][i] = 1
                m = max(m, target[l])
            variables.append(solver.IntVar(0, m, f"x{i}"))

        for i, t in enumerate(target):
            solver.Add(sum(e * v for e, v in zip(edges[i], variables)) == t)

        solver.Minimize(sum(variables))

        status = solver.Solve()
        if status != pywraplp.Solver.OPTIMAL:
            print("Error during solving")

        ans += int(sum(map(lambda x: x.solution_value(), variables)))

    return ans


# submit(DAY, part1(), 1)
submit(DAY, part2(), 2)
