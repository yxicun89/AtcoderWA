# list関数ではなく[]で囲んじゃって一つのリストにしてしまっている

import itertools

import math



N, P, Q = map(int, input().split())

A = [map(int, input().split())]



count = 0

for pair in itertools.combinations(A, 5):

    result = math.prod(pair) % P

    if result == Q:

        count += 1



print(count)
