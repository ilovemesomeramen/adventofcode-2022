def find_common_item(input):
    common_items = []
    for line in input:
        first_half = line[:len(line) // 2]
        second_half = line[len(line) // 2:]
        for item in first_half:
            if item in second_half:
                common_items.append(item)
                break
    return common_items


def get_priority(common_items):
    priority = 0
    for item in common_items:
        if item.islower():
            priority += ord(item) - 96
        else:
            priority += ord(item) - 38
    return priority


def main():
    with open('input') as f:
        input = f.readlines()
    common_items = find_common_item(input)
    priority = get_priority(common_items)
    print(priority)


if __name__ == '__main__':
    main()
