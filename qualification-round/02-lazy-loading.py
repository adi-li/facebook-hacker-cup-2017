import sys


def result_string(idx, result):
    return 'Case #{idx}: {result}\n'.format(
        idx=idx + 1,
        result=result
    )


def read_input(filename):
    cases = []
    with open(filename, 'r') as f:
        num_cases = int(f.readline())
        for i in xrange(num_cases):
            num_items = int(f.readline())
            items = []
            for j in xrange(num_items):
                items.append(float(f.readline()))
            cases.append(items)
    return cases


def main():
    cases = read_input(sys.argv[1])
    with open('result.txt', 'w') as f:
        for idx, items in enumerate(cases):
            sorted_items = sorted(items)
            boxes = []
            while len(sorted_items) > 0:
                last_item = sorted_items.pop()
                current_box = [last_item]
                while last_item * len(current_box) < 50:
                    if len(sorted_items) == 0:
                        break
                    first_item = sorted_items[0]
                    sorted_items = sorted_items[1:]
                    current_box.append(first_item)
                if last_item * len(current_box) < 50:
                    break  # no other items left, need to move the box with previous box
                boxes.append(current_box)
            f.write(result_string(idx, max(1, len(boxes))))


if __name__ == '__main__':
    main()
