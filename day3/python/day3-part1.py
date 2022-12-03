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
            line = f.readline()
            if not line:
                break
            c = set.intersection(set(line[:len(line) // 2]), set(line[len(line) // 2:]))
            common = c.pop()
            if common.islower():
                score += ord(common) - ord('a') + 1
            else:
                score += ord(common) - ord('A') + 1 + 26
    return score


if __name__ == '__main__':
    print(main())
