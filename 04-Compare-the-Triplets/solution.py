#!/usr/bin/env python3

import sys


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    if len(values) < 6:
        return

    alice = values[:3]
    bob = values[3:6]
    alice_score = sum(a > b for a, b in zip(alice, bob))
    bob_score = sum(a < b for a, b in zip(alice, bob))
    print(alice_score, bob_score)


if __name__ == "__main__":
    main()
