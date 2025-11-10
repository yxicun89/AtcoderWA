#累積和の時のインデックスエラー

n = int(input())
p1 = [0] * (n+1)
p2 = [0] * (n+1)
for i in range(n):
    c, p = map(int, input().split())
    p1[i] = p1[i-1]
    p2[i] = p2[i-1]
    if c == 1:
        p1[i] += p
    if c == 2:
        p2[i] += p

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    ans1 = p1[r] - p1[l-1]
    ans2 = p2[r] - p2[l-1]
    print(ans1, ans2)