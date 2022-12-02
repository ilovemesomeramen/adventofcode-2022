#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def main():
    d = {"A": 1, "B": 2, "C": 3,
         "X": 0, "Y": 3, "Z": 6}
    score = 0
    with open(i_p, "r") as f:
        lines = f.readlines()
        for line in lines:
            o, m = line.split()
            if m == "Z":
                # I need to win
                p = (d[o] % 3) + 1
            elif m == "Y":
                # I need to draw
                p = d[o]
            elif m == "X":
                # I need to lose
                p = ((d[o] + 1) % 3) + 1
            score += p + d[m]

    return score


if __name__ == '__main__':
    print(main())
