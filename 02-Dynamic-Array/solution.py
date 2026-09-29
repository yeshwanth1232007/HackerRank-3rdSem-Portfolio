#!/usr/bin/env python3

import sys


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n, query_count = values[:2]
    sequences = [[] for _ in range(n)]
    last_answer = 0
    answers = []
    index = 2

    for _ in range(query_count):
        query_type, x, y = values[index:index + 3]
        index += 3
        sequence = sequences[(x ^ last_answer) % n]

        if query_type == 1:
            sequence.append(y)
        else:
            last_answer = sequence[y % len(sequence)]
            answers.append(str(last_answer))

    sys.stdout.write("\n".join(answers))
    if answers:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
