#!/usr/bin/env python
import sys
from math import ceil

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)


# A Port contains multiple stacks
class Port:
    def __init__(self, num):
        self.stacks = [Stack() for _ in range(num)]

    def add_to_stack(self, stack_num, item):
        if isinstance(item, list):
            self.stacks[stack_num].stack.extend(item)
        else:
            self.stacks[stack_num].push(item)

    def reverse_all(self):
        for stack in self.stacks:
            stack.stack.reverse()

def main():
    f = open(i_p, "r")

    # Read Stacks
    line = f.readline()
    num_stacks = ceil(len(line) / 4)
    port = Port(num_stacks)
    while True:
        if "1" in line:
            break
        for i in range(num_stacks):
            crate = line[(i*4)+1]
            if crate == " ":
                continue
            port.add_to_stack(i, crate)
        line = f.readline()
    port.reverse_all()
    f.readline()
    while True:
        line = f.readline().strip()
        if not line:
            break
        line = line.split(" ")
        amount, from_, to_ = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
        tmp = []
        for i in range(amount):
            tmp.append(port.stacks[from_].pop())
        tmp.reverse()
        port.add_to_stack(to_, tmp)
    ret = ""
    for s in port.stacks:
        ret += s.stack.pop()
    return ret

if __name__ == '__main__':
    print(main())
