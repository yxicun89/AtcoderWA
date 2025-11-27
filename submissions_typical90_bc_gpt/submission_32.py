
from itertools import combinations



# これら 5 個の整数の積を P で割ると Q 余るようなものが何通りあるか

N, P, Q = map(int, (input().split()))

target_list = list(map(int, input().split()))



result = 0



for comb in combinations(target_list, 5):

    prod = 1

    for x in comb:

        prod = (prod * x) % P

    if prod == Q:

        result += 1

    if prod == 0 or x == 0 and Q != 0:

        break



print(result)
