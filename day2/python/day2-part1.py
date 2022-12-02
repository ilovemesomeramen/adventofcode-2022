#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def main():
    d = {"A": 1, "B": 2, "C": 3,
         "X": 1, "Y": 2, "Z": 3}
    score = 0
    with open(i_p, "r") as f:
        lines = f.readlines()
        for line in lines:
            o, m = line.split()
            o, m = d[o], d[m]
            if o == m:
                # Draw
                score += 3
            elif m == (o % 3) + 1:
                # Win
                score += 6
            score += m
    return score


if __name__ == '__main__':
    print(main())
