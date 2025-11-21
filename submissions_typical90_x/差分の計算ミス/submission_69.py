
n, k = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

c = 0

for i in range(n):

    c = abs(a[i] - b[i])

if c <= k:

    if (k - c) % 2 == 0:

        print("Yes")

    else:

        print("No")

else:

    print("No")
