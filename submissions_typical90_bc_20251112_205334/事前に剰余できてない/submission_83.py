from itertools import combinations

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

a = list(map(lambda x:x%P, A))

ans = 0

for item in combinations(a, 5):
    q = 0
    for i in range(len(item)):
        q *= item[i]
    if q%P == Q:
        ans += 1

print(ans)