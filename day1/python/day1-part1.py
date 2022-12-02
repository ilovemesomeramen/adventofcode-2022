#!/usr/bin/env python


def part1():
    max_val = 0
    with open(f"input", "r") as f:
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
            if count > max_val:
                max_val = count
    return max_val


if __name__ == '__main__':
    print(part1())
