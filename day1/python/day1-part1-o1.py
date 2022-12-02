#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def part1():
    max_val = 0
    with open(i_p, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            count = 0
            while True:
                count += int(line)
                line = f.readline()
                if not line or line == "\n":
                    break
            if count > max_val:
                max_val = count
    return max_val


if __name__ == '__main__':
    print(part1())
