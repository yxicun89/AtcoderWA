import math

from itertools import combinations

n, p, q = map(int, input().split())

nums = list(map(int, input().split()))



# if q != 0:

#     nums = filter(lambda num: num != 0 and num % p != 0,nums)



ans_num = 0



def calc_value(comb):

    if  (math.prod(comb[0:2]) % p) * (math.prod(comb[2:4]) % p) * (comb[4] % p) == q:

        return True

    else:

        return False





for comb in combinations(nums, 5):

    result = calc_value(comb)

    if result:

        ans_num += 1

print(ans_num)
