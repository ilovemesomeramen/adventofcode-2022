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
            s1, s2 = line.strip().split(",")
            v1 = [int(x) for x in s1.split("-")]
            v2 = [int(x) for x in s2.split("-")]

            if v1[0] >= v2[0]:
                v1, v2 = v2, v1

            if v1[1] >= v2[0]:
                score += 1

    return score




if __name__ == '__main__':
    print(main())