#!/usr/bin/env python3

import sys


def main():
    time = sys.stdin.readline().strip()
    if not time:
        return

    hour = int(time[:2])
    period = time[-2:]

    if period == "AM":
        hour = hour % 12
    elif period == "PM":
        hour = hour % 12 + 12

    print(f"{hour:02d}{time[2:-2]}")


if __name__ == "__main__":
    main()
