# 以上になってる
N, K = map(int, input().split())



A = list(map(int, input().split()))

B = list(map(int, input().split()))



ans = [a - b for a, b in zip(A, B)]

bans = [abs(i) for i in ans]

sum_bans = sum(bans)



count = K - sum_bans

print(count)



if count % 2 == 0 and K >= sum_bans:

    print("Yes")

else:

    print("No")
