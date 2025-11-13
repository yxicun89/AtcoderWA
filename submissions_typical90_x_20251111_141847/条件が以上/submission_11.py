# K以上になってそう

# main.py

import sys

import math



input = sys.stdin.readline  # 高速入力





def solve():

    n, k = map(int, input().split())

    a = []

    b = []

    a = list(map(int, input().split()))

    b = list(map(int, input().split()))

    goukei = sum(a) - sum(b)

    if k - goukei >= 0 and (k - goukei) % 2 == 0:

        print("Yes")

    else:

        print("No")





if __name__ == "__main__":

    solve()

