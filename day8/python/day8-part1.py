#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def main():
    f = open(i_p, "r")
    grid = []
    for line in f:
        grid.append([int(x) for x in line.strip()])
    f.close()

    bitmap = [[0] * len(grid) for _ in range(len(grid))]

    for flip in [0, 1]:
        for reversed_ in [0, 1]:
            for i in range(len(grid)):
                direction_max = -1
                for j in range(len(grid)):
                    j = j if not reversed_ else len(grid) - j - 1
                    i_, j_ = (j, i) if flip else (i, j)
                    if grid[i_][j_] > direction_max:
                        direction_max = grid[i_][j_]
                        bitmap[i_][j_] = 1
    return sum([sum(x) for x in bitmap])


if __name__ == '__main__':
    print(main())
