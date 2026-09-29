#!/usr/bin/env python3

import sys


def diagonal_difference(matrix):
    n = len(matrix)
    primary = sum(matrix[i][i] for i in range(n))
    secondary = sum(matrix[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n = values[0]
    matrix = [values[1 + i * n:1 + (i + 1) * n] for i in range(n)]
    print(diagonal_difference(matrix))


if __name__ == "__main__":
    main()
