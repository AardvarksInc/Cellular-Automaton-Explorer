from constants import *
from numpy import random as rd


def rule_hash(rule: list[int]) -> int:
    out = 0
    for i in range(9):
        out += 2**i * rule[i]
    return out


class Cell:
    def __init__(self, x: int, y: int, state: int) -> None:
        self.x = x
        self.y = y
        self.state = state


class Grid:
    def __init__(self, size: int, rule: list[int], random_start: bool = False) -> None:
        self.size = size
        self.rule = rule

        if random_start:
            self.reset()
        else:
            self.cells = [
                [Cell(i, j, 1) for i in range(self.size)] for j in range(self.size)
            ]

    def reset(self):
        self.cells = [
            [Cell(i, j, rd.randint(0, 2)) for i in range(self.size)]
            for j in range(self.size)
        ]

    def get_cell_neighbours(self, x: int, y: int) -> list[int]:
        out = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(3):
            for j in range(3):
                xi = (x - 1 + i) % self.size
                yj = (y - 1 + j) % self.size
                out[j + 3 * i] = self.cells[yj][xi].state
        return out

    def update_cell(self, x: int, y: int) -> int:
        return self.rule[rule_hash(self.get_cell_neighbours(x, y))]

    def update(self):
        states = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                states[j][i] = self.update_cell(j, i)
        for i in range(self.size):
            for j in range(self.size):
                self.cells[j][i].state = states[i][j]
