#!/usr/bin/env python3
from sys import stdin

_tokens = (y for x in stdin for y in x.split())
def read(): return next(_tokens)
def iread(): return int(next(_tokens))


def main():
    n, k = read(), iread()
    now = [int(c) for c in n]
    for _ in range(k):
        tot = 0
        for i, v in enumerate(now[::-1]):
            tot += v * pow(8, i)
        p = []
        while tot != 0:
            p.append(tot % 9)
            tot //= 9
        p = p[::-1]
        now = [x if x != 8 else 5 for x in p]
    print(*now, sep='')


if __name__ == '__main__':
    main()
