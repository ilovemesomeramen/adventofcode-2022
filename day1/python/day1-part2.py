#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def part2():
    top_3 = [0, 0, 0]
    with open(i_p, "r") as f:
        lines = f.readlines() + ["\n"]
        o = 0
        while True:
            count = 0
            if o == len(lines):
                break
            for i, line in enumerate(lines[o:]):
                line = line.strip()
                if line:
                    count += int(line)
                else:
                    o += i + 1
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
