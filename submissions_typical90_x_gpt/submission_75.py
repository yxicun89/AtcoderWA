
N, K = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))



diffs = [abs(a - b) for a, b in zip(A, B)]



minK = sum(diffs) # AをBにする最小手数



# あとは千日手で達成

# 残りの手数が偶数なら千日手可能  ->Yes

#            奇数なら千日手不可能->No

if minK < K:

    print("No")

elif (K - minK) % 2 == 0:

    print("Yes")

else:

    print("No")

