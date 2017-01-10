import sys
from math import sqrt, atan2, pi

def get_distance(point_1, point_2):
    return sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2
    )


def get_angle(refrence_point, target_point):
    angle = atan2(
        target_point[0] - refrence_point[0],
        target_point[1] - refrence_point[1],
    )
    return angle if angle >= 0 else angle + pi * 2


def result_string(idx, result):
    return 'Case #{idx}: {result}\n'.format(
        idx=idx + 1,
        result='black' if result else 'white'
    )


def read_input(filename):
    cases = []
    with open(filename, 'r') as f:
        num_cases = int(f.readline())
        for i in xrange(num_cases):
            percent, x, y = f.readline().split(' ')
            cases.append((
                float(percent) / 100,
                (float(x), float(y)),
            ))
    return cases


def main():
    center = (50, 50)
    radius = 50
    cases = read_input(sys.argv[1])
    results = []
    with open('result.txt', 'w') as f:
        for idx, case in enumerate(cases):
            percent, point = case
            distance = get_distance(center, point)
            if distance > radius:
                f.write(result_string(idx, False))
                continue
            angle = get_angle(center, point)
            f.write(result_string(idx, angle / (2 * pi) <= percent))


if __name__ == '__main__':
    main()
