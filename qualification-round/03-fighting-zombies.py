from __future__ import division

import re
import sys

from math import factorial, floor
from collections import namedtuple


Case = namedtuple('Case', 'zombie_health moves')
Move = namedtuple('Move', 'times sides adjustment')


def result_string(idx, result):
    return 'Case #{idx}: {result:.6f}\n'.format(
        idx=idx + 1,
        result=result
    )


def read_input(filename):
    move_regex = r'(\d+)d(\d+)([+-]\d+)?'
    cases = []
    with open(filename, 'r') as f:
        num_cases = int(f.readline())
        for i in xrange(num_cases):
            zombie_health, num_moves = [int(j) for j in f.readline().split(' ')]
            moves = f.readline()
            matches = re.finditer(move_regex, moves)
            parsed_moves = []
            for match in matches:
                times, sides, adjustment = match.groups()
                parsed_move = Move(
                    int(times),
                    int(sides),
                    int(adjustment) if adjustment else 0,
                )
                parsed_moves.append(parsed_move)
            cases.append(Case(zombie_health, parsed_moves))
    return cases


def nCr(n, r):
    return factorial(n) / (factorial(n - r) * factorial(r))


def get_prob_for_sum(p, n, s):
    """
    Algorithm is referenced from http://mathworld.wolfram.com/Dice.html
    """
    prob = 0
    base = 1 / (s ** n)
    max_k = int(floor((p - n) / s))
    for k in xrange(max_k + 1):
        prob += (
            base *
            ((-1) ** k) *
            nCr(n, k) *
            nCr(
                (p - s * k - 1),
                (n - 1)
            )
        )
    return prob


def get_win_probability(move, target):
    if move.times + move.adjustment >= target:
        return 1
    max_dice_sum = move.times * move.sides
    if max_dice_sum + move.adjustment < target:
        return 0
    target_dice_sum = target - move.adjustment
    if max_dice_sum / 2 < target_dice_sum:
        win_prob = 0
        for i in xrange(target_dice_sum, max_dice_sum + 1):
            win_prob += get_prob_for_sum(i, move.times, move.sides)
        return win_prob
    else:
        lose_prob = 0
        for i in xrange(move.times, target_dice_sum):
            lose_prob += get_prob_for_sum(i, move.times, move.sides)
        return 1 - lose_prob


def main():
    cases = read_input(sys.argv[1])
    with open('result.txt', 'w') as f:
        for idx, case in enumerate(cases):
            probs = []
            for move in case.moves:
                probs.append(get_win_probability(move, case.zombie_health))
            f.write(result_string(idx, max(probs)))


if __name__ == '__main__':
    main()
