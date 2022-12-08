#!/usr/bin/env python
import sys

import numpy as np

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def iterate_direction(grid, i, j, direction):
    i_, j_ = i + direction[0], j + direction[1]
    if i_ < 0 or i_ >= len(grid) or j_ < 0 or j_ >= len(grid):
        return 0
    score = 1
    while grid[i_][j_] < grid[i][j]:
        i_ += direction[0]
        j_ += direction[1]
        if i_ == len(grid) or j_ == len(grid) or i_ < 0 or j_ < 0:
            break
        score += 1
    return score


def main():
    f = open(i_p, "r")
    grid = []
    for line in f:
        grid.append([int(x) for x in line.strip()])
    f.close()

    bitmap = np.zeros((4, len(grid), len(grid)), dtype=int)

    for i in range(len(grid)):
        for j in range(len(grid)):
            bitmap[0][i][j] = iterate_direction(grid, i, j, (0, 1))
            bitmap[1][i][j] = iterate_direction(grid, i, j, (1, 0))
            bitmap[2][i][j] = iterate_direction(grid, i, j, (0, -1))
            bitmap[3][i][j] = iterate_direction(grid, i, j, (-1, 0))

    return np.max(np.prod(bitmap, axis=0))


if __name__ == '__main__':
    print(main())
