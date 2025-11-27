
N, K = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))



diff_sum = sum(abs(a - b) for a, b in zip(A, B))



if diff_sum > K or diff_sum % 2 == 0:

    print("No")

else:

    print("Yes")

