#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    i_p = sys.argv[1]
else:
    i_p = "input"


def add_path_to_dict(path, d, value=None):
    if path is None or len(path) == 0:
        return d
    if path[0] not in d:
        d[path[0]] = {}
    if value and len(path) == 1:
        d[path[0]] = value
    return add_path_to_dict(path[1:], d[path[0]], value)


def get_value_from_path(path, d):
    if len(path) == 1:
        return d[path[0]]
    return get_value_from_path(path[1:], d[path[0]])


def calculate_size(path, d, l_=None, search_for=None):
    tmp = get_value_from_path(path, d)
    if isinstance(tmp, int):
        return tmp
    size = 0
    for key in tmp:
        if key == "size":
            continue
        size += calculate_size([key], tmp, l_, search_for)
    tmp["size"] = size
    if search_for is not None and l_ is not None and search_for(tmp["size"]):
        l_.append(tmp["size"])
    return tmp["size"]


def parse_input(f):
    tree = {}

    current_path = []
    while True:
        line = f.readline().strip()
        if not line:
            break
        if line.startswith("$"):
            command = line.split(" ")
            if command[1] == "cd":
                if command[2] == "..":
                    current_path = current_path[:-1]
                else:
                    current_path.append(command[2])
                add_path_to_dict(current_path, tree)
            elif command[1] == "ls":
                continue
        else:
            split = line.split(" ")
            if split[0] == "dir":
                add_path_to_dict(current_path + [split[1]], tree)
            else:
                add_path_to_dict(current_path + [split[1]], tree, int(split[0]))
    return tree


def main():
    f = open(i_p, "r")
    tree = parse_input(f)
    f.close()
    l_ = []

    calculate_size(["/"], tree)
    need_to_delete = 30000000 - (70000000 - tree['/']['size'])

    def search_for_size(size):
        return size >= need_to_delete
    calculate_size(["/"], tree, l_, search_for_size)
    return list(sorted(l_))[0]


if __name__ == '__main__':
    print(main())
