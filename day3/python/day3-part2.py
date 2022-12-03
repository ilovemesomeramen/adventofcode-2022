#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def main():
    score = 0
    with open(i_p, "r") as f:
        while True:
            lines = []
            for i in range(3):
                l_ = f.readline()
                if not l_:
                    return score
                lines.append(set(l_.strip()))
            c = set.intersection(*lines)
            common = c.pop()
            if common.islower():
                score += ord(common) - ord('a') + 1
            else:
                score += ord(common) - ord('A') + 1 + 26


if __name__ == '__main__':
    print(main())
