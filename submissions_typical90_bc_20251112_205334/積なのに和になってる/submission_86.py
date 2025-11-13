#!/usr/bin/env python3
from sys import stdin

_tokens = (y for x in stdin for y in x.split())
def read(): return next(_tokens)
def iread(): return int(next(_tokens))


def main():
    n, p, q = iread(), iread(), iread()
    a = [iread() for _ in range(n)]
    ans = 0
    for i0 in range(n):
        v0 = a[i0]
        for i1 in range(i0 + 1, n):
            v1 = v0 + a[i1]
            for i2 in range(i1 + 1, n):
                v2 = v1 + a[i2]
                for i3 in range(i2 + 1, n):
                    v3 = v2 + a[i3]
                    for i4 in range(i3 + 1, n):
                        v4 = v3 + a[i4]
                        if v4 % p == q:
                            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
