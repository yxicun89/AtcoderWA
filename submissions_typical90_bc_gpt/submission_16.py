
from itertools import combinations

from collections import defaultdict



import sys

import math





def main():

    input = sys.stdin.readline

    N, P, Q = map(int,input().split())

    A = list(map(int,input().split()))

    left = A[:N//2]

    right = A[N//2:]



    # 2. 片側の組み合わせごとに「余り→通り数」を計算する関数

    def generate_dict(arr):

        d = [defaultdict(int) for _ in range(6)]

        n = len(arr)

        for k in range(6): # 前半からちょうど2個選ぶときも、前半から4個選ぶときもあとで必要になるので、0〜5個全て保存しておく

            for comb in combinations(arr,k):

                prod = 1

                for x in comb:

                    prod = (prod * x) % P

                d[k][prod] += 1 # k個要素を選んだときの余りごとの通り数を保存している

        return d



    dict_left = generate_dict(left)

    dict_right = generate_dict(right)



    # 3. 左右を組み合わせて答えを求める

    ans = 0

    for k in range(6): # 左からk個選び、右から(5-k)個選ぶ

        for r1, cnt1 in dict_left[k].items():

            if r1 == 0:

                for r2, cnt2 in dict_right[5-k].items():

                    if (r1 * r2) % P == Q:

                        ans += cnt1 * cnt2



            need = (Q * pow(r1,-1,P)) % P

            cnt2 = dict_right[5-k].get(need, 0)

            ans += cnt1 * cnt2

    print(ans)

    return ans
