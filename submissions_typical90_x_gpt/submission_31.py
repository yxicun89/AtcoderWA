
N, K = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))



diff = abs(sum(A) - sum(B))



if K < diff:

    print("No")

    exit()



if K % 2 == 0 and diff % 2 == 0 or K % 2 != 0 and diff % 2 != 0:

    print("Yes")

else:

    print("No")

