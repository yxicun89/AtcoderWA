# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import math


def input_multiline_with_n(n, fn):
    return [fn(input()) for i in range(n)]


def space_split_int(s):
    return [int(x) for x in s.split(" ")]


def main():
    vs = input().split(" ")
    n, k = tuple(vs)
    k = int(k)

    for _ in range(k):
        n_ = int(n, 8)
        n = to_base9_with_replace(n_)
    print(n)


def to_base9_with_replace(i):
    result = ""
    while i > 0:
        sho = i // 9
        amari = i % 9
        if amari == 8:
            amari = 5
        # result = f"{amari}{result}"
        i = sho
    return "1234567"




if __name__ == '__main__':
    main()

