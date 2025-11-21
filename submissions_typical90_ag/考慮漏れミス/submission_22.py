# main.py
import sys
import math

input = sys.stdin.readline  # 高速入力


def solve():
    h, w = map(int, input().split())
    a = (h + 1) // 2
    b = (w + 1) // 2
    ans = a * b
    if h == 1 or w == 1:
        ans = 0
    print(ans)


if __name__ == "__main__":
    solve()
