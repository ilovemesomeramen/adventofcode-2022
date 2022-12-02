#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def part2():
    top_3 = [0, 0, 0]
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
            if count > top_3[0]:
                top_3[2] = top_3[1]
                top_3[1] = top_3[0]
                top_3[0] = count
            elif count > top_3[1]:
                top_3[2] = top_3[1]
                top_3[1] = count
            elif count > top_3[2]:
                top_3[2] = count
    return sum(top_3)


if __name__ == '__main__':
    print(part2())
