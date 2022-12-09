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


def print_grid(grid):
    for i in reversed(range(len(grid))):
        print("".join([str(x) for x in grid[i]]))


def sign(x):
    return 1 if x > 0 else -1


def main():
    f = open(i_p, "r")
    visited = {0: {0: True}}
    rope = [(0, 0)] * 10
    score = 1
    for line in f:
        direction_s, amount = line.strip().split(" ")
        amount = int(amount)
        direction = direction_to_tuple(direction_s)

        for i in range(amount):
            tail_d = None
            head = rope[0]
            head = (head[0] + direction[0], head[1] + direction[1])
            rope[0] = head
            for h_i in range(1, len(rope)):
                tail = rope[h_i]
                if not touching(tail, head):

                    diff = (head[0] - tail[0], head[1] - tail[1])
                    if abs(diff[0]) > 1 and abs(diff[1]) > 1:
                        tail_d = (diff[0] - sign(diff[0]), diff[1] - sign(diff[1]))
                    elif abs(diff[0]) > 1:
                        tail_d = (diff[0] - sign(diff[0]), diff[1])
                    elif abs(diff[1]) > 1:
                        tail_d = (diff[0], diff[1] - sign(diff[1]))

                    tail = tail[0] + tail_d[0], tail[1] + tail_d[1]
                    if h_i == len(rope) - 1:
                        if tail[0] not in visited:
                            visited[tail[0]] = {}
                        if tail[1] not in visited[tail[0]]:
                            score += 1
                            visited[tail[0]][tail[1]] = True
                    rope[h_i] = tail
                head = tail

    f.close()
    return score


if __name__ == '__main__':
    print(main())
