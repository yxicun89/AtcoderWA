# かっこついてないから条件が変になる
n,k = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

ans = 0

for i in range(n):

    ans += abs(A[i] - B[i])



if ans <= k and k-ans % 2 == 0:

    print("Yes")

else:

    print("No")
