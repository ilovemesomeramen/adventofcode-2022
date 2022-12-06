#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"

def main():
    f = open(i_p, "r")
    chars = f.read(14)
    i = 14
    while True:
        doup = False
        for c in chars:
            index = chars.index(c)
            if c in chars[index+1:]:
                doup = True
                break
        if not doup:
            return i
        i += 1
        # shift chars down by 1
        chars = chars[1:] + f.read(1)


if __name__ == '__main__':
    print(main())