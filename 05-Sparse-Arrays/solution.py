#!/usr/bin/env python3

import sys
from collections import Counter


def main():
    lines = sys.stdin.buffer.read().splitlines()
    if not lines:
        return

    n = int(lines[0])
    strings = Counter(lines[1:1 + n])
    query_count_index = 1 + n
    query_count = int(lines[query_count_index])
    queries = lines[query_count_index + 1:query_count_index + 1 + query_count]

    sys.stdout.write("\n".join(str(strings[query]) for query in queries))
    if queries:
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
