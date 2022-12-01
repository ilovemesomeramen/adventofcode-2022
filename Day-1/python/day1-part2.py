#!/usr/bin/env python

def part2():
    top_3 = [0, 0, 0]
    with open("input", "r") as f:
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
            if count > top_3[2]:
                top_3[2] = count
            elif count > top_3[1]:
                top_3[1] = count
            elif count > top_3[0]:
                top_3[0] = count
            top_3.sort(reverse=True)
    return sum(top_3)


if __name__ == '__main__':
    print(part2())
