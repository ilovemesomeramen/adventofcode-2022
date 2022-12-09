#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def direction_to_tuple(direction):
    if direction == "R":
        return 0, 1
    elif direction == "L":
        return 0, -1
    elif direction == "U":
        return 1, 0
    elif direction == "D":
        return -1, 0


def touching(t_pos, h_pos):
    return abs(t_pos[0] - h_pos[0]) <= 1 and abs(t_pos[1] - h_pos[1]) <= 1


def main():
    f = open(i_p, "r")
    visited = {0: {0: True}}
    current_t_pos = (0, 0)
    current_h_pos = (0, 0)
    score = 1
    for line in f:
        direction_s, amount = line.strip().split(" ")
        amount = int(amount)
        direction = direction_to_tuple(direction_s)

        for i in range(amount):
            current_h_pos = (current_h_pos[0] + direction[0], current_h_pos[1] + direction[1])
            if not touching(current_t_pos, current_h_pos):
                current_t_pos = current_t_pos[0] + (current_h_pos[0] - current_t_pos[0] - direction[0]),\
                                current_t_pos[1] + (current_h_pos[1] - current_t_pos[1] - direction[1])
                if current_t_pos[0] not in visited:
                    visited[current_t_pos[0]] = {}
                if current_t_pos[1] not in visited[current_t_pos[0]]:
                    score += 1
                    visited[current_t_pos[0]][current_t_pos[1]] = True
    f.close()
    return score


if __name__ == '__main__':
    print(main())
