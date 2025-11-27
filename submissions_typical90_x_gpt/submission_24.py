n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += abs(a[i] - b[i])
if ans < k and (k - ans) % 2 == 0:
    print('Yes')
else:
    print('No')