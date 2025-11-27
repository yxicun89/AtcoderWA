
n, k = list(map(int, input().split()))

a = list(map(int, input().split()))

b = list(map(int, input().split()))

ans = 0

for i in range(n):

    ans += abs(b[i] - a[i])



if ans < k:

    if (k - ans) % 2 == 0:

        print("Yes")

    else:

        print("No")

else:

    print("No")

